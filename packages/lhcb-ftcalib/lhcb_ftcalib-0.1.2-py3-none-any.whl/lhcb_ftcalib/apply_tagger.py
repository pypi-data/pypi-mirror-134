import json
import pandas as pd
import numpy as np

from lhcb_ftcalib.Tagger import TaggerBase
from lhcb_ftcalib.calibration_functions import PolynomialCalibration
from lhcb_ftcalib.combination import combine_taggers
from lhcb_ftcalib.TaggingData import TaggingData
from lhcb_ftcalib.printing import (info, section_header, printbold, raise_warning, print_tagger_correlation,
                                   print_tagger_performances, print_tagger_statistics, warning,
                                   raise_error)
import lhcb_ftcalib.link_functions as links
from lhcb_ftcalib.plotting import draw_inputcalibration_curve
from lhcb_ftcalib.performance import p_conversion_matrix


class TargetTaggerCollection:
    r""" class TaggerCollection List type for grouping target taggers. Supports iteration.

        :param \*taggers: Tagger instance
        :type \*taggers: Tagger
    """
    def __init__(self, *taggers):
        self._taggers = [*taggers]
        self._index = -1
        if self._taggers:
            self._validate()

    def __str__(self):
        return "TargetTaggerCollection [" + ','.join([t.name for t in self._taggers]) + "]"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self._taggers)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index == len(self._taggers) - 1:
            self._index = -1
            raise StopIteration
        self._index += 1
        return self._taggers[self._index]

    def __getitem__(self, t):
        return self._taggers[t]

    def _validate(self):
        assert all([isinstance(tagger, TargetTagger) for tagger in self]), "TaggerCollection can only store TargetTagger instances"
        assert len(set([tagger.name for tagger in self])) == len(self._taggers), "Tagger names are not unique"

    def add_taggers(self, *tagger):
        """ Adds tagger(s) to the TargetTaggerCollection instance """
        self._taggers += [*tagger]
        self._validate()

    def create_tagger(self, *args, **kwargs):
        """ Adds a TargetTagger instance to the TargetTaggerCollection instance
            by passing the arguments to the TargetTagger() constructor.
        """
        self._taggers.append(TargetTagger(*args, **kwargs))
        self._validate()

    def load_calibrations(self, filename, tagger_mapping=None, style="flavour"):
        """ Load calibrations from a file

            :param filename: Filename of the calibration file
            :type filename: str
            :param tagger_mapping: Optional dictionary of a mapping of tagger names in this list vs corresponding entry names in the calibration file. By default, the same naming is assumed (!)
            :type tagger_mapping: dict
            :param style: Which parameter style to use
            :type style: str ("delta", "flavour")
        """
        if tagger_mapping is None:
            tagger_mapping = { t.name : t.name for t in self }
        else:
            assert len(tagger_mapping) == len(self)

        for tagger in self:
            info(f"Loading {tagger_mapping[tagger.name]} calibrations for {tagger.name}")
            tagger.load(filename, tagger_mapping[tagger.name], style)

    def apply(self, quiet=False, ignore_delta=True):
        """ Applies the previously loaded calibrations to a taggers

            :param quiet: Whether to print performance summary tables
            :type quiet: bool
        """

        if not quiet:
            print_tagger_correlation(self, "fire",       selected=True)
            print_tagger_correlation(self, "dec",        selected=True)
            print_tagger_correlation(self, "dec_weight", selected=True)
            print_tagger_statistics(self, calibrated=False, selected=False)
            print_tagger_performances(self, calibrated=False, selected=False)

        for tagger in self:
            info(f"Applying calibration for {tagger.name}")
            tagger.apply(ignore_delta)

        if not quiet:
            print_tagger_statistics(self, calibrated=True, selected=False)
            print_tagger_performances(self, calibrated=True, selected=False)

    def get_dataframe(self, calibrated=True):
        """ Returns a dataframe of the calibrated mistags and tagging decisions

            :return: Calibrated data
            :return type: pandas.DataFrame
        """
        df = pd.DataFrame()
        if calibrated:
            for tagger in self:
                assert tagger.is_calibrated()
                df[tagger.name + "_CDEC"] = np.array(tagger.cstats.all_dec.copy(), dtype=np.int32)
                df[tagger.name + "_OMEGA"] = tagger.cstats.all_eta.copy()
        else:
            for tagger in self:
                df[tagger.name + "_DEC"] = np.array(tagger.stats.all_dec.copy(), dtype=np.int32)
                df[tagger.name + "_ETA"] = tagger.stats.all_eta.copy()

        return df

    def plot_inputcalibration_curves(self, **kwargs):
        r""" Plots input calibration curves of a set of taggers, like the EPM
            does when a calibration is applied.  Plots the loaded calbration curve
            (uncertainties are loaded but ignored while applying the calibration)
            and the targeted mistag data.

            :param \**kwargs: Arguments to pass to draw_inputcalibration_curve
        """
        for tagger in self:
            print("Info: pdf file", draw_inputcalibration_curve(tagger, **kwargs), "has been created")

    def combine_taggers(self, name, calibrated):
        """ Computes the combination of multiple taggers
            and returns it in the form of a new Tagger object

            :param name: Name of the tagger combination
            :type name: str
            :param calibrated: Whether to use calibrated tagger data for combination (recommended)
            :type calibrated: bool
            :return: Tagger combination
            :rtype: Tagger
        """
        taggernames = [t.name for t in self]
        section_header("TAGGER COMBINATION")
        printbold("Combining taggers " + " ".join(taggernames) + f" into {name}")
        printbold("Checking compatibility")

        # Sanity checks
        raise_warning(name not in taggernames, "Name of combination is already in use")
        if calibrated:
            indeed_calibrated = [t.is_calibrated() is not None for t in self]  # Do not forbid combination of calibrated and uncalibrated taggers
            raise_warning(all(indeed_calibrated), "None, or not all provided taggers have been calibrated")

        printbold("Running combination...")
        # Collect data
        if calibrated:
            decs   = np.array([ np.array(tagger.cstats.all_dec if cal else tagger.stats.all_dec) for tagger, cal in zip(self._taggers, indeed_calibrated) ]).T
            omegas = np.array([ np.array(tagger.cstats.all_eta if cal else tagger.stats.all_eta) for tagger, cal in zip(self._taggers, indeed_calibrated) ]).T
        else:
            decs   = np.array([ np.array(tagger.stats.all_dec) for tagger in self ]).T
            omegas = np.array([ np.array(tagger.stats.all_eta) for tagger in self ]).T

        d_combined, omega_combined = combine_taggers(decs, omegas)

        # Construct Tagger object
        combination = TargetTagger(name     = name,
                                   eta_data = omega_combined,
                                   dec_data = d_combined,
                                   weight = self._taggers[0].stats.all_weights)
        printbold(f"New tagger combination {combination.name} has been created")
        return combination


class TargetTagger(TaggerBase):
    """ A variation of the tagger object which loads a calibration
        from file and applies it to some data. Like the "Tagger",
        it contains two sets of TaggingData (BasicTaggingData) for
        before and after the calibration.

        Note: Specifying the B id, calibration mode,
        decay time and its uncertainty as well as the resolution model is
        optional and only needed in order to estimate the raw mistag if this performance
        number is needed and if it makes sense to compute it from the B ids in the tuple.

        :param name: Name of this target tagger. Ideally, try to use the same as for the calibrated tagger
        :type name: str
        :param eta: Targeted mistag data
        :type eta: list
        :param dec: Targeted tagging decisions
        :type dec: list
        :param weight: Weight variable (needed for tagging statistics information)
        :type weight: list

        :param mode: Calibration mode (Not needed)
        :type mode: str
        :param ID: B meson IDs (Not needed)
        :type ID: list
        :param tau: Decay times in ps (Not needed)
        :type tau: list
        :param tauerr: Decay time uncertainties in ps (Not needed)
        :type tauerr: list
    """
    class __MinimizerView:
        def __init__(self):
            self.covariance = None

    def __init__(self, name, eta_data, dec_data, B_ID=None, mode=None, tau_ps=None, tauerr_ps=None, weight=None, resolution_model=None, DM=None, DG=None):
        raise_error(not (mode in ("Bd", "Bs") and tau_ps is None), "If a \"calibration\" mode is specified for a target tagger, the decay time needs to be provided")
        raise_error(not (mode is None and any([a is not None for a in [tau_ps, tauerr_ps, resolution_model, DM, DG]])),
                    "If decay time related info is provided for a target tagger, the mode must be set to Bd or Bs")

        if tau_ps is not None and B_ID is None:
            warning("Need B ID to use decay time info. Ignoring tau branch.")

        super().__init__(name              = name,
                         eta_data          = eta_data,
                         dec_data          = dec_data,
                         B_ID              = B_ID if B_ID is not None else np.ones(len(eta_data)),
                         mode              = "Bu" if mode is None else mode,
                         tau_ps            = tau_ps if B_ID is not None else None,
                         tauerr_ps         = tauerr_ps if B_ID is not None else None,
                         weight            = weight,
                         selection         = np.ones(len(eta_data), dtype=bool),  # All events are selected when taggers are applied
                         resolution_model  = resolution_model,
                         analytic_gradient = False,
                         DM                = DM,
                         DG                = DG)
        self.info        = None
        self.cstats      = None
        self.func        = None  # TaggerBase sets func by default
        self._calibrated = False
        self._has_b_id   = B_ID is not None
        self.minimizer   = self.__MinimizerView()

    def apply(self, ignore_delta=True):
        """ Apply the previously loaded calibration to this tagger """
        assert self._calibrated
        omega = 0.5 * np.ones(self.stats.N)

        if ignore_delta:
            omega[self.stats.tagged] = self.func.eval_ignore_delta(self.params_nominal, self.stats.eta, self.stats.avg_eta)
        else:
            omega[self.stats.tagged] = self.func.eval(self.params_nominal, self.stats.eta, self.stats.dec, self.stats.avg_eta)
        self.cstats = TaggingData(eta_data = omega,
                                  dec_data  = self.stats.all_dec.copy(),
                                  ID        = self.stats.all_B_ID.copy(),
                                  tau       = self.stats.all_tau.copy() if self.mode in ("Bd", "Bs") else None,
                                  tauerr    = self.stats.all_tauerr.copy() if self.stats.all_tauerr is not None else None,
                                  weights   = self.stats.all_weights.copy(),
                                  selection = np.ones(self.stats.N, dtype=bool))
        self._calibrated = True

    def get_dataframe(self, calibrated=True):
        """ Returns a dataframe of the calibrated mistags and tagging decisions

            :return: dataframe with calibrated tagging decisions and mistags
            :return type: pandas.DataFrame
            :raises: AssertionError if calibration has not yet been applied
        """
        if calibrated:
            assert self._calibrated
            return pd.DataFrame({
                self.name + "_CDEC"  : np.array(self.cstats.all_dec.copy(), dtype=np.int32),
                self.name + "_OMEGA" : self.cstats.all_eta.copy()
            })
        else:
            return pd.DataFrame({
                self.name + "_DEC"  : np.array(self.stats.all_dec.copy(), dtype=np.int32),
                self.name + "_ETA" : self.stats.all_eta.copy()
            })

    def get_fitparameters(self, style="delta", p1minus1=False, tex=False, greekdelta=False):
        """ Returns arrays of parameter names, nominal values
            and uncertainties and covariance matrix of a loaded Tagger

            :param style: Which parameter convention to use
            :type style: str ("delta", "flavour")
            :param p1minus1: Whether to subtract 1 from p1
            :type p1minus1: bool
            :param tex: Whether to format parameter names as tex
            :type tex: bool
            :param greekdelta: Whether to use "D" or "Δ" (only if tex=False)
            :type greekdelta: bool

            :return: Tuple (parameters, nominal_values, uncertainties, covariance matrix)
            :return type: tuple
        """
        if not self._calibrated:
            return None

        noms    = self.params_nominal.copy()
        uncerts = self.params_uncerts.copy()
        params  = self.func.param_names.copy()
        cov     = self.minimizer.covariance.copy()
        npar    = self.func.npar

        if style == "delta":
            conv_mat = p_conversion_matrix(npar)
            params = [p.replace("+", "").replace("-", "") for p in params]
            for i, p in enumerate(params[npar:]):
                params[i + npar] = "D" + p

            # Transform uncertainties
            noms  = conv_mat @ noms
            cov = conv_mat @ np.array(cov.tolist()) @ conv_mat.T
            uncerts = np.sqrt(np.diag(cov))

            if p1minus1:
                if len(noms) >= 4:
                    noms[1] += 1
        elif style == "flavour":
            if p1minus1:
                if len(noms) >= 4:
                    noms[1] -= 1
                    noms[npar + 1] -= 1

        if tex:
            params = [p.replace("p", "p_").replace("+", "^+").replace("-", "^-") for p in params]
            params = [p.replace("D", r"\Delta ") for p in params]
        else:
            if greekdelta:
                params = [p.replace("D", "Δ") for p in params]

        return params, noms, uncerts, cov

    def load(self, filename, tagger_name, style="flavour"):
        """ Load a calibration entry from a calibration file

            :param filename: Filename of the calibration file
            :type filename: str
            :param tagger_name: Entry name of the calibration data you would like to load
            :type tagger_name: str
            :param style: Which parameter style to use
            :type style: str ("delta", "flavour")
        """
        with open(filename, "r") as F:
            calib = json.loads(F.read())

        # Reconstruct calibration function
        assert tagger_name in calib, "Tagger " + tagger_name + " not contained in calibration file"
        self.info = calib[tagger_name]

        assert style in ["flavour", "delta"], "Calibrations in " + style + "style not supported. Please use 'flavour' or 'delta' style."

        if "PolynomialCalibration" in self.info:
            fun_info = self.info["PolynomialCalibration"]
            self.func = PolynomialCalibration(int(fun_info["degree"]) + 1, get_link_by_name(fun_info["link"]))
            params = np.array([self.info["calibration"][style + "_style"]["params"][p] for p in (self.func.param_names if style == "flavour" else self.func.param_names_delta)])
            noms = [float(v) for v in params[:, 0]]
            uncerts = [float(v) for v in params[:, 1]]
            cov = self.info["calibration"][style+"_style"]["cov"]
            cov = np.array([float(e) for row in cov for e in row]).reshape((2 * self.func.npar, 2 * self.func.npar))
            if style == "delta":
                # convert delta_style to flavour_style
                conv_mat = np.linalg.inv(p_conversion_matrix(self.func.npar)) # Use inverted matrix, because matrix is designed for inverse conversion
                noms     = conv_mat @ noms
                cov      = conv_mat @ np.array(cov.tolist()) @ conv_mat.T
                uncerts  = np.sqrt(np.diag(cov))
            self.params_nominal = noms
            self.params_uncerts = uncerts

            self.stats.avg_eta = float(self.info["calibration"]["avg_eta"])  # Always use avg_eta from calibrations
            self.minimizer.covariance = cov

            self.DeltaM     = self.info["osc"]["DeltaM"]
            self.DeltaGamma = self.info["osc"]["DeltaGamma"]
            self.Aprod      = self.info["osc"]["Aprod"]
        else:
            raise NotImplementedError

        self._calibrated = True


def get_link_by_name(link):
    return {
        "mistag"   : links.mistag,
        "logit"    : links.logit,
        "rlogit"   : links.rlogit,
        "probit"   : links.probit,
        "rprobit"  : links.rprobit,
        "cauchit"  : links.cauchit,
        "rcauchit" : links.rcauchit,
    }[link]
