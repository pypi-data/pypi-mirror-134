import numpy as np
import uncertainties
import pandas as pd

pd.set_option("display.max_rows", 30)
pd.set_option("display.max_columns", 30)
pd.set_option("display.width", 1000)

from lhcb_ftcalib.calibration_functions import PolynomialCalibration
from lhcb_ftcalib.performance import tagging_rate, mean_mistag, tagging_power, tagger_correlation


def blue_header(msg):
    print('\033[1m\033[94m' + (len(msg) + 5) * "/")
    print(4 * "/", msg, "\033[0m")


def printbold(msg, kwargs={}):
    # Blue EPM style paragraph title frame
    print('\033[1m\033[97m' + msg + "\033[0m", **kwargs)


def correlation_header(msg):
    # EPM style correlation header
    print(80 * '/' + f"\n\033[1m{msg} [%]\033[0m\n" + 80 * '/')


def section_header(msg, bold=True):
    # EPM style section header
    if bold:
        print('\n\033[1m' + (len(msg) + 32) * "-")
    else:
        print((len(msg) + 32) * "-")
    print(15 * '-' + f" {msg} " + 15 * '-')
    print((len(msg) + 32) * "-" + '\033[0m\n')


def warning(*msg):
    print("\033[1m\033[33m WARNING \033[0m", *msg)


def info(*msg):
    print("\033[1m\033[97m INFO \033[0m", *msg)


def raise_warning(cond, msg):
    if not cond:
        print(f"\033[1m\033[33m WARNING:\033[0m {msg}")


def raise_error(cond, msg):
    if not cond:
        print(f"\033[1m\033[31m ERROR:\033[0m {msg}")
        raise AssertionError


class FTCalibException(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(msg)

    def __str__(self):
        return f"\033[1m\033[31m ERROR:\033[0m {self.msg}"


class MissingFile(FTCalibException):
    pass


class MissingTree(FTCalibException):
    pass


class MissingBranch(FTCalibException):
    pass


class PerfTable:
    """ Formatted table for summarising performances """
    def __init__(self, headers, tagger_names, pad=2, round_digits=4):
        self.headers = headers
        self.tagger_names = tagger_names
        self.pad = pad
        self.percentages = False
        self.round_digits = round_digits

        self.data = []

    def fill_row(self, values):
        assert len(values) == len(self.headers)
        assert isinstance(values, list)
        self.data.append(values)

    def print_percentages(self):
        self.percentages = True

    def __str__(self):
        assert len(self.data) == len(self.tagger_names)
        # Format data

        def vformat(v):
            return np.round(v, self.round_digits)

        uvalue = f"{{:>{self.round_digits + 3}}} ± {{:>{self.round_digits + 2}}}"
        for r, row in enumerate(self.data):
            for c, val in enumerate(row):
                if isinstance(val, uncertainties.UFloat):
                    if self.percentages:
                        self.data[r][c] = "(" + uvalue.format(vformat((100 * val).n), vformat((100 * val).s)) + ")%"
                    else:
                        self.data[r][c] = uvalue.format(vformat(val.n), vformat(val.s))
                elif isinstance(val, float):
                    self.data[r][c] = vformat(val)
                else:
                    self.data[r][c] = str(val)

        self.data = np.array(self.data)

        pad = self.pad * " "
        # Format rows
        maxtagname = max(len("Tagger"), *[len(t) for t in self.tagger_names])
        min_colwidths = [ max(len(h), *[len(d) for d in self.data[:, i]]) for i, h in enumerate(self.headers)]
        rowformat  = f"\033[32m{{:>{maxtagname}}}\033[0m"
        rowformat += pad + "".join([f"{{:<{mc}}}{pad}" for mc in min_colwidths]) + "\n"

        # Format header
        header = f"\033[1m\033[32m{{:>{maxtagname}}}" + pad
        header += pad.join([f"{{:>{cw}}}" for cw in min_colwidths]) + "\033[0m\n"
        header = header.format("Tagger", *self.headers)

        body = ""
        for t, name in enumerate(self.tagger_names):
            body += rowformat.format(name, *self.data[t])

        return header + body


def print_tagger_statistics(taggers, calibrated, selected=True):
    """ Prints basic statistics of the input data for each tagger

        :param taggers: List of taggers
        :type taggers: list
        :param calibrated: Whether to show calibrated tagger statistics (after calibration)
        :type calibrated: bool
    """
    from lhcb_ftcalib.apply_tagger import TargetTagger, TargetTaggerCollection
    if calibrated:
        section_header("CALIBRATED TAGGER STATISTICS", bold=True)
    else:
        section_header("RAW TAGGER STATISTICS", bold=False)

    if isinstance(taggers, TargetTagger) or isinstance(taggers, TargetTaggerCollection) and selected:
        warning("Selected statistics unavailable for TargetTaggers (selected=True), setting to False")
        selected = False

    tagnames = [t.name for t in taggers]
    tab = PerfTable(["#Evts (N)", "weighted Σw", "(Σw)² / Σw²", "#Tagged", "Σ_tag * w"], tagnames)
    if selected:
        for t in taggers:
            if calibrated:
                tab.fill_row([t.cstats.Ns, t.cstats.Nws, t.cstats.Neffs, t.cstats.Nts, t.cstats.Nwts])
            else:
                tab.fill_row([t.stats.Ns, t.stats.Nws, t.stats.Neffs, t.stats.Nts, t.stats.Nwts])
    else:
        for t in taggers:
            if calibrated:
                tab.fill_row([t.cstats.N, t.cstats.Nw, t.cstats.Neff, t.cstats.Nt, t.cstats.Nwt])
            else:
                tab.fill_row([t.stats.N, t.stats.Nw, t.stats.Neff, t.stats.Nt, t.stats.Nwt])

    print(tab)


def print_tagger_performances(taggers, calibrated=False, selected=True, round_digits=4):
    """ Prints a table with standard performance numbers like the tagging rate,
        the mistag rate and the tagging power for each tager

        :param taggers: List of taggers
        :type taggers: list
        :param calibrated: Whether to show calibrated tagger statistics (after calibration)
        :type calibrated: bool
        :param selected: Whether to only use events in selection
        :type selected: bool
        :param round_digits: Number of digits to round to
        :type round_digits: int
    """
    tagnames = [t.name for t in taggers]
    if calibrated:
        section_header("CALIBRATED TAGGING PERFORMANCES", bold=True)
        tab = PerfTable(["Tagging Rate", "Mistag", "Tagging Power"], tagnames)
        for tagger in taggers:
            tab.fill_row([tagging_rate(tagger, calibrated, selected),
                          mean_mistag(tagger, calibrated, selected),
                          tagging_power(tagger, calibrated, selected)])
    else:
        section_header("RAW TAGGING PERFORMANCES", bold=False)
        tab = PerfTable(["Tagging Rate", "Mistag", "Tagging Power"], tagnames)
        for tagger in taggers:
            tab.fill_row([tagging_rate(tagger, calibrated, selected),
                          mean_mistag(tagger, calibrated, selected),
                          tagging_power(tagger, calibrated, selected)])

    tab.print_percentages()
    print(tab)


def print_tagger_correlation(taggers, option="all", calibrated=False, selected=False):
    """ Print different kinds of tagger correlations. By default, all correlations are printed

        :param taggers: List of taggers
        :type taggers: list
        :param option: Type of correlation to compute ("fire", "dec", "dec_weight")
        :type option: string
    """
    if selected:
        info("Correlations of selected events")
    if option in ("all", "fire"):
        correlation_header("Tagger Fire Correlations")
        print(100 * tagger_correlation(taggers, "fire", selected=selected, calibrated=calibrated), '\n' + 80 * '/', '\n')
    if option in ("all", "dec"):
        correlation_header("Tagger Decision Correlations")
        print(100 * tagger_correlation(taggers, "dec", selected=selected, calibrated=calibrated), '\n' + 80 * '/', '\n')
    if option in ("all", "dec_weight"):
        correlation_header("Tagger Decision Correlations (dilution weighted)")
        print(100 * tagger_correlation(taggers, "dec_weight", selected=selected, calibrated=calibrated), '\n' + 80 * '/', '\n')
    if option in ("all", "both_fire"):
        correlation_header("Tagger Decision Correlations (If both fire)")
        print(100 * tagger_correlation(taggers, "both_fire", selected=selected, calibrated=calibrated), '\n' + 80 * '/', '\n')


def print_calibration_info(tagger):
    """ Prints the obtained calibration parameters of a tagger after it has been calibrated

        :param taggers: List of taggers
        :type taggers: list
    """
    from lhcb_ftcalib.Tagger import Tagger
    assert tagger.is_calibrated()

    def fmt(val, uncert):
        return "{:>10} ± {:>9}".format(np.round(val, 7), np.round(uncert, 7))

    if isinstance(tagger, Tagger):
        blue_header(f"Calibration result of {tagger.name}")
    else:
        blue_header(f"{tagger.name} Calibration (Loaded)")
    printbold("=== Oscillation parameters ===")
    print(f"Δm    = {tagger.DeltaM} ps^-1")
    print(f"ΔΓ    = {tagger.DeltaGamma} ps^-1")
    print(f"Aprod = {tagger.Aprod}")
    printbold("=== Result in flavour specific representation ===")
    ps, noms, uncerts, cov = tagger.get_fitparameters(style="flavour", p1minus1=False, tex=False, greekdelta=False)

    for name, val, uncert in zip(ps, noms, uncerts):
        print(f"{name}", fmt(val, uncert))
    print("<η> =", tagger.stats.avg_eta)

    if isinstance(tagger.func, PolynomialCalibration):
        printbold("=== Result in p_i, Δp_i convention ===")
        # "EPM printing convention"
        ps, noms, uncerts, cov = tagger.get_fitparameters(style="delta", p1minus1=False, tex=False, greekdelta=True)

        for name, val, uncert in zip(ps, noms, uncerts):
            print(f"{name}", fmt(val, uncert))
        print("<η> =", tagger.stats.avg_eta)
