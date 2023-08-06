import numpy as np
import pandas as pd
from numba import jit
from uncertainties import ufloat


def p_conversion_matrix(npar):
    r""" Returns matrix :math:`C` that converts internal representation of
        parameters into the traditional form
        :math:`C\cdot (p^+_0,\cdots, p^+_n, p^-_0,\cdots,p^-_n) = (p_0,\cdots, p_n, \Delta p_0,\cdots,\Delta p_n)`

        :param npar: number of calibration parameters per flavour
        :type npar: int
        :return: parameter transformation
        :rtype: numpy.ndarray
    """
    upper = np.concatenate([0.5 * np.eye(npar), 0.5 * np.eye(npar)]).T
    lower = np.concatenate([np.eye(npar), -np.eye(npar)]).T
    return np.concatenate([upper, lower])


def tagging_rate(tagger, calibrated, selected=True):
    r""" Returns the tagging efficiency with binomial uncertainty
        :math:`\epsilon_{\mathrm{tag}}=N_t/N`

        :param stats: Tagger stats
        :type stats: TaggingData
        :param calibrated: Whether to use calibrated mistag and decisions
        :type calibrated: bool
        :param selected: Whether to only use events in selection
        :type selected: bool
        :return: Tagging efficiency
        :rtype: ufloat
    """
    if calibrated:
        assert tagger.is_calibrated()
        if selected:
            N, Nt, Neff = tagger.cstats.Nws, tagger.cstats.Nwts, tagger.cstats.Neffs
        else:
            N, Nt, Neff = tagger.cstats.Nw, tagger.cstats.Nwt, tagger.cstats.Neff
    else:
        if selected:
            N, Nt, Neff = tagger.stats.Nws, tagger.stats.Nwts, tagger.stats.Neffs
        else:
            N, Nt, Neff = tagger.stats.Nw, tagger.stats.Nwt, tagger.stats.Neff

    rate     = Nt / N
    untagged = N - Nt
    return ufloat(rate, np.sqrt(Nt * untagged / Neff) / N)


def mean_mistag(tagger, calibrated, selected=True):
    r""" Returns mean mistag of selected statistics with binomial uncertainty
        :math:`\langle\omega\rangle=N_{\mathrm{wrong}} / N`


        :param tagger: Tagger
        :type tagger: Tagger
        :param calibrated: Whether to use calibrated mistag and decisions
        :type calibrated: bool
        :param selected: Whether to use selected statistics. (Must be true)
        :type selected: bool
        :return: Mistag rate
        :rtype: ufloat
    """
    if not selected:
        return "unavailable"

    if calibrated:
        assert tagger.is_calibrated()
        Nright = np.sum(tagger.cstats.weights[tagger.cstats.correct_tags])
        Nwrong = np.sum(tagger.cstats.weights[tagger.cstats.wrong_tags])
        Nweighted = tagger.cstats.Nwts
    else:
        Nright = np.sum(tagger.stats.weights[tagger.stats.correct_tags])
        Nwrong = np.sum(tagger.stats.weights[tagger.stats.wrong_tags])
        Nweighted = tagger.stats.Nwts

    return ufloat(Nwrong / (Nwrong + Nright), np.sqrt(Nright * Nwrong / Nweighted) / Nweighted)


def tagging_power(tagger, calibrated, selected=True):
    r""" Computes the effective tagging efficiency

        :math:`\displaystyle\epsilon_{\mathrm{tag},\mathrm{eff}} = \frac{\epsilon_{\mathrm{tag}}}{\sum_{i, \mathrm{tagged}} w_i}\sum_{i, \mathrm{tagged}}w_i(1-2\eta_i)^2`

        :param tagger: Tagger
        :type tagger: Tagger
        :param calibrated: Whether to use calibrated mistag instead of raw mistag
        :type calibrated: bool
        :param selected: Whether to only use events in selection
        :type selected: bool
        :return: Tagging power
        :rtype: ufloat
    """

    tagrate = tagging_rate(tagger, calibrated, selected)

    if selected:
        if calibrated:
            assert tagger.is_calibrated()
            D = np.array(1 - 2 * tagger.cstats.eta)
            mean_D_sq = np.sum(D**2 * tagger.cstats.weights) / tagger.cstats.Nwts  # tagpower of tagged events

            # Propagate errors of mean dilution squared
            grad_calib = tagger.func.gradient(tagger.params_nominal, tagger.cstats.eta, tagger.cstats.dec, tagger.stats.avg_eta)
            grad_mean_D_sq  = -4 * np.sum(grad_calib * D * np.array(tagger.cstats.weights), axis=1) / tagger.cstats.Nwts
            mean_D_sq_err = np.sqrt(grad_mean_D_sq @ tagger.minimizer.covariance.tolist() @ grad_mean_D_sq.T)

            tagpower = tagrate * ufloat(mean_D_sq, mean_D_sq_err)
        else:
            D = 1 - 2 * tagger.stats.eta
            mean_D_sq = np.sum(D**2 * tagger.stats.weights) / tagger.stats.Nwts  # tagpower of tagged events

            tagpower = tagrate * mean_D_sq
    else:
        # Events that are only tagged are not quite as accessible, but that does not really matter
        if calibrated:
            tagged = tagger.cstats.tagged
            eta    = tagger.cstats.all_eta[tagged]
            dec    = tagger.cstats.all_dec[tagged]
            weight = tagger.cstats.all_weights[tagged]

            assert tagger.is_calibrated()
            D = np.array(1 - 2 * eta)
            mean_D_sq = np.sum(D**2 * weight) / tagger.cstats.Nwt  # tagpower of tagged events

            # Propagate errors of mean dilution squared
            grad_calib = tagger.func.gradient(tagger.params_nominal, eta, dec, tagger.stats.avg_eta)  # stats.avg_eta is correct
            grad_mean_D_sq  = -4 * np.sum(grad_calib * D * np.array(weight), axis=1) / tagger.cstats.Nwt
            mean_D_sq_err = np.sqrt(grad_mean_D_sq @ tagger.minimizer.covariance.tolist() @ grad_mean_D_sq.T)

            tagpower = tagrate * ufloat(mean_D_sq, mean_D_sq_err)
        else:
            tagged = tagger.stats.tagged
            eta    = tagger.stats.all_eta[tagged]
            dec    = tagger.stats.all_dec[tagged]
            weight = tagger.stats.all_weights[tagged]
            D = 1 - 2 * eta
            mean_D_sq = np.sum(D**2 * weight) / tagger.stats.Nwt  # tagpower of tagged events

            tagpower = tagrate * mean_D_sq
    return tagpower


def tagger_correlation(taggers, corrtype="dec_weight", selected=True, calibrated=False):
    r""" Compute different kinds of tagger correlations. The data points are weighted by their per-event weight.
        The weighted correlation coefficient between two observables X and Y with weights W is defined as

        :math:`\displaystyle\mathrm{corr}(X, Y, W) = \frac{\mathrm{cov}(X, Y, W)}{\mathrm{cov}(X, X, W) \mathrm{cov}(Y, Y, W)}`

        whereby

        :math:`\mathrm{cov}(X, Y, W) = \displaystyle\sum_i w_i (x_i-\overline{X}) (y_i - \overline{Y}) / \sum_iw_i`

        and

        :math:`\overline{X} = \sum_i w_ix_i / \sum_i w_i`

        One can choose between 4 different correlation types:

        * corrtype="fire" : Correlation of tagger decisions irrespective of decision sign
            :math:`x_i=|d_{x,i}|, y_i=|d_{y,i}|` and :math:`W` is the event weight

        * corrtype="dec" : Correlation of tagger decisions taking sign of decision into account
            :math:`x_i=d_{x,i}, y_i=d_{y,i}` and :math:`W` is the event weight

        * corrtype="dec_weight" : Correlation of tagger decisions taking sign of decision into account and weighted by tagging dilution
            :math:`x_i=d_{x,i}(1-2\eta_{x,i}), y_i=d_{y,i}(1-2\eta_{y,i}),` and :math:`W` is the event weight

        * corrtype="both_fire" : Correlation of tagger decisions if both have fired taking sign of decision into account
            :math:`x_i=d_{x,i}, y_i=d_{y,i}` and :math:`W` is the event weight

        :param taggers: List of taggers
        :type taggers: list
        :param corr: Type of correlation
        :type corr: string
        :param selected: Whether to only use events in selection
        :type selected: bool
        :param calibrated: Whether to use calibrated statistics. (Only relevant for correlation types with mistag, not part of automatic print-out)
        :type calibrated: bool
        :return: Correlation matrix
        :rtype: pandas.DataFrame
    """

    @jit(nopython=True)
    def corr(X, Y, W):
        Neff = np.sum(W)
        avg_X = np.sum(X * W) / Neff
        avg_Y = np.sum(Y * W) / Neff
        Xres = X - avg_X
        Yres = Y - avg_Y
        covXY = np.sum(W * Xres * Yres) / Neff
        covXX = np.sum(W * Xres * Xres) / Neff
        covYY = np.sum(W * Yres * Yres) / Neff
        return covXY / np.sqrt(covXX * covYY)

    N = len(taggers)
    m_corr = np.ones((N, N)) * -999  # If something is not filled, show -999

    class getter:
        def __init__(self, stats):
            self.stats = stats

        def __call__(self, tagger, attr):
            return np.array(getattr(getattr(tagger, self.stats), attr)[getattr(tagger, self.stats).selected])

    get = getter("cstats" if calibrated else "stats")

    for x, TX in enumerate(taggers):
        for y, TY in enumerate(taggers[x:]):
            if TX.name == TY.name:
                m_corr[x][x + y] = 1
                continue
            if calibrated:
                assert TY.is_calibrated()
            if corrtype == "fire":
                try:
                    m_corr[x][x + y] = corr(np.abs(get(TX, "all_dec")),
                                            np.abs(get(TY, "all_dec")),
                                            get(TX, "all_weights"))
                except ZeroDivisionError:
                    m_corr[x][x + y] = np.nan
            elif corrtype == "dec":
                m_corr[x][x + y] = corr(get(TX, "all_dec"),
                                        get(TY, "all_dec"),
                                        get(TX, "all_weights"))
            elif corrtype == "dec_weight":
                m_corr[x][x + y] = corr(get(TX, "all_dec") * (1 - 2 * get(TX, "all_eta")),
                                        get(TY, "all_dec") * (1 - 2 * get(TY, "all_eta")),
                                        get(TX, "all_weights"))
            elif corrtype == "both_fire":
                d1 = get(TX, "all_dec")
                d2 = get(TY, "all_dec")
                mask = (d1 != 0) & (d2 != 0)
                m_corr[x][x + y] = corr(d1[mask], d2[mask], get(TX, "all_weights")[mask])

            m_corr[x + y][x] = m_corr[x][x + y]

    names = [tagger.name for tagger in taggers]
    m_corr = pd.DataFrame({name : m_corr[n] for n, name in enumerate(names)}, index = names)
    return m_corr
