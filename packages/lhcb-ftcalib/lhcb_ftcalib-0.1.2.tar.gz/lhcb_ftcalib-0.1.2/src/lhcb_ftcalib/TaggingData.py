import numpy as np
import pandas as pd

from lhcb_ftcalib.printing import raise_error, raise_warning
from lhcb_ftcalib.resolution_model import mixing_asymmetry


def get_absid(ID):
    ids = ID.abs().unique()
    ids = list(ids[ids != 0])
    raise_error(len(ids) > 0, f"There are no nonzero particle IDs in the ID branch {ids}")
    raise_error(len(ids) == 1, f"There are too many particle IDs in the ID branch: {ids}")
    raise_warning(ids[0] in (511, 521, 531), f"Particle ID {ids[0]} does not belong to a Bu, Bd or Bs meson")
    return ids[0]


class TaggingData:
    r"""
    TaggingData
    Type for keeping track of tagging data and basic event statistics

    :param eta_data: Uncalibrated mistags
    :type eta_data: list
    :param dec_data: Uncalibrated tagging decisions
    :type dec_data: list
    :param ID: B meson particle IDs
    :type ID: list
    :param tau: Decay time in picoseconds
    :type tau: list
    :param tauerr: Decay time uncertainty in picoseconds
    :type tauerr: list
    :param weights: Per-event weights
    :type weights: list
    """
    def __init__(self, eta_data, dec_data, ID, tau, tauerr, weights, selection):
        # Init full tagging data (Copy to avoid spooky action at a distance)
        self.all_eta    = pd.Series(eta_data, copy=True)                  #: All eta values
        self.all_dec    = pd.Series(dec_data, dtype=np.int32, copy=True)  #: All dec values
        self.all_B_ID   = pd.Series(ID, copy=True)                        #: All B meson IDs
        self.selected   = pd.Series(selection, copy=True)                 #: Mask of events in selection
        if tau is not None:
            self.all_tau = pd.Series(tau, copy=True)  #: All decay time values
        else:
            self.all_tau = None
        if tauerr is not None:
            self.all_tauerr = pd.Series(tauerr, copy=True)  #: All decay time uncertainty values
        else:
            self.all_tauerr = None

        # Reset indices so that from now on everything is guaranteed to be aligned
        # (pd.Series copy constructor preserves alignment)
        self.all_eta.reset_index(drop=True, inplace=True)
        self.all_dec.reset_index(drop=True, inplace=True)
        self.all_B_ID.reset_index(drop=True, inplace=True)
        self.selected.reset_index(drop=True, inplace=True)
        if self.all_tau is not None:
            self.all_tau.reset_index(drop=True, inplace=True)
        if self.all_tauerr is not None:
            self.all_tauerr.reset_index(drop=True, inplace=True)

        # Memorize which events are overflow
        self.overflow  = (self.all_eta > 0.5)  #: Mask of events with :math:`\omega>0.5`
        self.underflow = (self.all_eta < 0)    #: Mask of events with :math:`\omega<0`
        self.noverflow = self.overflow.sum()   #: Number of calibrated mistags > 0.5

        self.tagged     = self.all_dec != 0                    #: Mask of tagged events
        self.tagged_sel = (self.all_dec != 0) & self.selected  #: Mask of selected and tagged events

        # Initialize tagged statistics for faster access (at the cost of memory consumption)
        self.dec        = pd.Series(self.all_dec[self.tagged_sel], dtype=np.int32)   #: Tagging decisions != 0 for selected events
        self.dec_flav   = pd.Series(self.all_B_ID[self.tagged_sel], dtype=np.int32)  #: B meson ids for tagged and selected candidates
        self.dec_flav   //= get_absid(self.dec_flav)
        self.prod_flav  = self.dec_flav.copy(deep=True)                              #: Production flavour estimate
        self.eta        = pd.Series(self.all_eta[self.tagged_sel])                   #: Mistag of tagged and selected candidates
        if self.all_tau is not None:
            self.tau = self.all_tau[self.tagged_sel]
        else:
            self.tau = None
        if self.all_tauerr is not None:
            self.tauerr = self.all_tauerr[self.tagged_sel]
        else:
            self.tauerr = None

        # Initialize yields and event weights
        self.N   = len(self.all_eta)      #: Number of events
        self.Ns  = self.selected.sum()    #: Number of selected events
        self.Nt  = self.tagged.sum()      #: Number of tagged events
        self.Nts = self.tagged_sel.sum()  #: Number of selected and tagged events

        if weights is None:
            self.weights = pd.Series(np.ones(self.Nts))  #: Event weight
        else:
            raise_error(len(weights) == self.N, "Tagging data must have matching dimensions")
            self.weights = pd.Series(weights, copy=True)[self.tagged & self.selected].copy(deep=True)
        self.weights.index = self.dec.index

        self.avg_eta    = np.average(self.eta, weights=self.weights)  #: Weighted average mistag of selected and tagged events

        self.all_weights = pd.Series(weights, copy=True) if weights is not None else np.ones(self.N)  #: All event weights
        self.Nw          = np.sum(self.all_weights)                  #: Weighted number of all events
        self.Neff        = self.Nw**2 / np.sum(self.all_weights**2)  #: Effective number of all events ((sum w)^2/(sum(w^2)))
        self.Nwt         = np.sum(self.all_weights[self.tagged])     #: Weighted number of all tagged events

        self.Nws         = np.sum(self.all_weights[self.selected])                   #: Weighted number of selected events
        self.Neffs       = self.Nws**2 / np.sum(self.all_weights[self.selected]**2)  #: Effective number selected events
        self.Nwts        = np.sum(self.weights)                                      #: Weighted number of selected and tagged events

        self.correct_tags = self.dec == self.prod_flav  #: Tag corresponds to production flavour (for selected events)
        self.wrong_tags   = ~self.correct_tags          #: Tag does not correspond to production flavour (for selected events)

        raise_error(self.Nt > 0 and self.Nts > 0 and self.Ns > 0, "No events left after cut = invalid tag data")
        self.tau = None
        self.tauerr = None
        self.__validate()

    def _init_timeinfo(self, mode, DM, DG, resolution_model):
        # Initialize tagged decay times
        if mode == "Bd":
            self.tau    = pd.Series(self.all_tau)[self.tagged_sel]  #: decay time in picoseconds
            self.tauerr = pd.Series(self.all_tauerr)[self.tagged_sel] if self.all_tauerr is not None else None  #: decay time uncertainty in picoseconds
        elif mode == "Bs":
            self.tau    = pd.Series(self.all_tau)[self.tagged_sel]
            self.tauerr = pd.Series(self.all_tauerr)[self.tagged_sel] if self.all_tauerr is not None else None
        elif mode == "Bu":
            self.tau    = None
            self.tauerr = None

        # Computes flavour impurity for each event. If oscillation probability
        # is > 50%, production flavour is assumed to be the opposite
        if mode == "Bu":
            self.osc_dilution = np.zeros(self.Nts)
            Amix = None
        else:
            Amix = mixing_asymmetry(self.tau[self.tagged_sel],
                                    DM     = DM,
                                    DG     = DG,
                                    tauerr = self.tauerr,
                                    a      = 0,
                                    res    = resolution_model)
            self.osc_dilution = 0.5 * (1.0 - np.abs(Amix))

        # Update production asymmetry given mixing asymmetry
        # and measures of "tag correctness"
        if mode != "Bu":
            self.prod_flav = self.dec_flav.copy()
            self.prod_flav[np.sign(Amix) == -1] *= -1

            self.correct_tags = self.dec == self.prod_flav
            self.wrong_tags   = ~self.correct_tags

        self.__validate()

    def __validate(self):
        # Check whether data is aligned
        assert len(self.all_eta)    == self.N
        assert len(self.all_dec)    == self.N
        assert len(self.all_B_ID)   == self.N
        assert len(self.selected)   == self.N
        assert len(self.tagged)     == self.N
        assert len(self.tagged_sel) == self.N

        assert len(self.eta)        == self.Nts
        assert len(self.dec)        == self.Nts
        assert len(self.prod_flav)  == self.Nts
        assert len(self.dec_flav)   == self.Nts
        if self.all_tau is not None:
            assert len(self.all_tau) == self.N
        if self.tau is not None:
            assert len(self.tau) == self.Nts
        if self.all_tauerr is not None:
            assert len(self.all_tauerr) == self.N
        if self.tauerr is not None:
            assert len(self.tauerr) == self.Nts

    def __str__(self):
        return ("Tagging Statistics\n"
                f"N  = {self.N}\n"
                f"Nw = {self.Nw}\n"
                f"Nt = {self.Nt}\n"
                f"Nwt = {self.Nwt}\n"
                f"Ns  = {self.Ns}\n"
                f"Nws = {self.Nws}\n"
                f"Nts = {self.Nts}\n"
                f"Nwts = {self.Nwts}")
