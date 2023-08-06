def test_modules():
    import importlib
    assert importlib.util.find_spec("lhcb_ftcalib")  is not None
    assert importlib.util.find_spec("iminuit")       is not None
    assert importlib.util.find_spec("numpy")         is not None
    assert importlib.util.find_spec("pandas")        is not None
    assert importlib.util.find_spec("uncertainties") is not None
    assert importlib.util.find_spec("flake8")        is not None
    assert importlib.util.find_spec("scipy")         is not None
    assert importlib.util.find_spec("numba")         is not None
    assert importlib.util.find_spec("matplotlib")    is not None

import os
import pytest
import itertools
import pandas as pd
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt

import lhcb_ftcalib as ft


class FakeMinimizer:
    def __init__(self, cov):
        self.covariance = cov


def test_syntax():
    from flake8.api import legacy as flake8
    style_guide = flake8.get_style_guide(ignore=["E221", "E402", "E501", "E251", "E203", "E201",
                                                 "E202", "E241", "E272", "E127", "E222", "E226",
                                                 "E722", "W503", "W291", "E265", "E266", "E303",
                                                 "E302", "E305", "E261"])
    pyfiles = ["Tagger.py", "TaggingData.py", "TaggerCollection.py", "link_functions.py",
               "calibration_functions.py", "plotting.py", "printing.py", "apply_tagger.py",
               "combination.py", "performance.py", "save_calibration.py", "__main__.py",
               "resolution_model.py"]

    pyfiles = [ "src/lhcb_ftcalib/" + py for py in pyfiles]
    report = style_guide.check_files(pyfiles)
    repF = report.get_statistics("F")
    repE = report.get_statistics("E")
    for rep in repF:
        print(rep)
    for rep in repE:
        print(rep)
    assert repF == []
    assert repE == []


def test_init_Bu():
    """ Check Tagger init values """
    name = "test1"
    df = pd.DataFrame({
        "eta"    : [0.2, 0.3, 0.4],
        "dec"    : [-1, 0, 1],
        "B_ID"   : [-521, 0, -521],
        "tau"    : [0.01, 0.02, 0.03],
        "tauerr" : [0.003, 0.002, 0.001],
        "weight" : [0.3, 0.2, 0.7]
    })
    df.dec = df.dec.astype(np.int32)
    mode = "Bu"
    tagged = df.dec != 0
    dec_flav  = pd.Series(df.B_ID[tagged] // 521, dtype=np.int32)
    prod_flav = pd.Series(dec_flav.copy(deep=True), dtype=np.int32)

    t = ft.Tagger(name      = name,
                  eta_data  = df.eta,
                  dec_data  = df.dec,
                  B_ID      = df.B_ID,
                  mode      = mode,
                  tau_ps    = df.tau,
                  tauerr_ps = df.tauerr,
                  weight    = df.weight)

    assert t.name == name
    assert t.mode == mode
    assert t.stats.tagged.equals(tagged)
    assert t.stats.dec.equals(pd.Series(df.dec[tagged], dtype=np.int32))
    assert t.stats.eta.equals(df.eta[tagged])
    assert t.stats.dec_flav.equals(dec_flav)
    assert t.stats.prod_flav.equals(prod_flav)
    assert np.isclose(t.stats.avg_eta, np.average(df.eta[tagged], weights=df.weight[tagged]))

    # Test oscillation params B+
    assert t.stats.tau is None
    assert t.stats.tauerr is None
    assert t.DeltaM is None
    assert t.DeltaGamma is None
    assert t.Aprod == 0

    # Test default calibration
    assert isinstance(t.func, ft.PolynomialCalibration)
    assert t.func.npar == 2
    assert t.func.link == ft.link_functions.mistag

    # Test tagger decisions
    assert t.stats.weights.equals(df.weight[tagged])
    assert t.stats.correct_tags.equals(prod_flav == df.dec[tagged])
    assert t.stats.wrong_tags.equals(prod_flav != df.dec[tagged])

    # Test tagger statistics
    assert t.stats.all_weights.equals(df.weight)
    assert t.stats.all_B_ID.equals(df.B_ID)
    assert t.stats.all_eta.equals(df.eta)
    assert t.stats.all_dec.equals(df.dec)

    assert t.stats.N == len(df)
    assert np.isclose(t.stats.Nw, np.sum(df.weight))
    assert np.isclose(t.stats.Neff, np.sum(df.weight)**2 / np.sum(df.weight**2))
    assert t.stats.Nt == tagged.sum()
    assert t.stats.Nwt == np.sum(df.weight[tagged])
    assert t.cstats is None


def test_init_Bd():
    """ Check Tagger init values """
    name = "test1"
    df = pd.DataFrame({
        "eta"    : [0.2, 0.3, 0.4],
        "dec"    : [-1, 0, 1],
        "B_ID"   : [-521, 0, -521],
        "tau"    : [0.01, 0.02, 0.03],
        "tauerr" : [0.003, 0.002, 0.001],
        "weight" : [0.3, 0.2, 0.7]
    })
    df.dec = df.dec.astype(np.int32)
    mode = "Bd"
    tagged = df.dec != 0
    dec_flav  = pd.Series(df.B_ID[tagged] // 521, dtype=np.int32)
    prod_flav = pd.Series(dec_flav.copy(deep=True), dtype=np.int32)

    t = ft.Tagger(name      = name,
                  eta_data  = df.eta,
                  dec_data  = df.dec,
                  B_ID      = df.B_ID,
                  mode      = mode,
                  tau_ps    = df.tau,
                  tauerr_ps = df.tauerr,
                  weight    = df.weight)

    assert t.name == name
    assert t.mode == mode
    assert t.stats.tagged.equals(tagged)
    assert t.stats.dec.equals(pd.Series(df.dec[tagged], dtype=np.int32))
    assert t.stats.eta.equals(df.eta[tagged])
    assert t.stats.dec_flav.equals(dec_flav)
    assert t.stats.prod_flav.equals(prod_flav)
    assert np.isclose(t.stats.avg_eta, np.average(df.eta[tagged], weights=df.weight[tagged]))

    # Test oscillation params B+
    assert t.stats.tau.equals(df.tau[tagged])
    assert t.stats.tauerr.equals(df.tauerr[tagged])
    assert isinstance(t.DeltaM, float)
    assert isinstance(t.DeltaGamma, float)
    assert t.Aprod == 0

    # Test default calibration
    assert isinstance(t.func, ft.PolynomialCalibration)
    assert t.func.npar == 2
    assert t.func.link == ft.link_functions.mistag

    # Test tagger decisions
    assert t.stats.weights.equals(df.weight[tagged])
    assert t.stats.correct_tags.equals(prod_flav == df.dec[tagged])
    assert t.stats.wrong_tags.equals(prod_flav != df.dec[tagged])

    # Test tagger statistics
    assert t.stats.all_weights.equals(df.weight)
    assert t.stats.all_B_ID.equals(df.B_ID)
    assert t.stats.all_eta.equals(df.eta)
    assert t.stats.all_dec.equals(df.dec)

    assert t.stats.N == len(df)
    assert np.isclose(t.stats.Nw, np.sum(df.weight))
    assert np.isclose(t.stats.Neff, np.sum(df.weight)**2 / np.sum(df.weight**2))
    assert t.stats.Nt == tagged.sum()
    assert t.stats.Nwt == np.sum(df.weight[tagged])
    assert t.cstats is None


def test_memory_addresses_Tagger():
    """ Test whether all dataframes are properly copied and memory cannot be externally corrupted """
    size = 100
    df = pd.DataFrame({
        "eta"    : np.random.uniform(0, 1, size),
        "dec"    : np.random.randint(-1, 2, size),
        "B_ID"   : 521 * np.random.randint(-1, 2, size),
        "tau"    : np.random.uniform(0, 1, size),
        "tauerr" : np.random.uniform(0, 1, size),
        "weight" : np.random.uniform(0, 1, size)
    })
    mode = "Bd"

    t = ft.Tagger(name      = "test",
                  eta_data  = df.eta,
                  dec_data  = df.dec,
                  B_ID      = df.B_ID,
                  mode      = mode,
                  tau_ps    = df.tau,
                  tauerr_ps = df.tauerr,
                  weight    = df.weight)

    # Test uniqueness of addresses (python happily defaults to copying references, which leads to data clones)
    attributes_stats = ["all_eta", "all_dec", "all_B_ID", "overflow",
                        "underflow", "tagged", "dec", "dec_flav",
                        "prod_flav", "eta", "avg_eta", "weights",
                        "all_weights", "correct_tags", "wrong_tags",
                        "tau", "tauerr", "all_tau", "all_tauerr"]
    addresses = [id(t.stats.__getattribute__(attr)) for attr in attributes_stats]
    assert len(set(addresses)) == len(addresses)

    # Test whether Tagger.get_fitparams() returns references
    t._calibrated = True
    t.params_nominal = [1, 2, 3, 4]
    t.params_uncerts = [3, 2, 1, 0]
    t.minimizer = FakeMinimizer(np.array([[1, 0, 0.1, 0.2],
                                          [0, 1, 0.1, 0.1],
                                          [0, 0, 1, 0],
                                          [0, 0, 0, 0.2]]))
    params, noms, uncerts, cov = t.get_fitparameters(style="flavour")
    assert id(noms)    != id(t.params_nominal)
    assert id(uncerts) != id(t.params_uncerts)
    assert id(cov)     != id(t.minimizer.covariance)
    params, noms, uncerts, cov = t.get_fitparameters(style="delta")
    assert id(noms)    != id(t.params_nominal)
    assert id(uncerts) != id(t.params_uncerts)
    assert id(cov)     != id(t.minimizer.covariance)


def test_init_list_types():
    """ Check whether Tagger initializes with different kinds of lists """
    def is_series(tagger):
        assert isinstance(tagger.stats.tagged,      pd.Series)
        assert isinstance(tagger.stats.dec,         pd.Series)
        assert isinstance(tagger.stats.dec_flav,    pd.Series)
        assert isinstance(tagger.stats.prod_flav,   pd.Series)
        assert isinstance(tagger.stats.eta,         pd.Series)
        assert isinstance(tagger.stats.weights,     pd.Series)
        assert isinstance(tagger.stats.all_weights, pd.Series)
        assert isinstance(tagger.stats.all_B_ID,    pd.Series)
        assert isinstance(tagger.stats.all_eta,     pd.Series)
        assert isinstance(tagger.stats.all_dec,     pd.Series)

    # Test whether tagger data ist matching
    def data_match(taggers):
        for t1, t2 in itertools.combinations(taggers, 2):
            assert list(t1.stats.tagged)      == list(t2.stats.tagged)
            assert list(t1.stats.dec)         == list(t2.stats.dec)
            assert list(t1.stats.dec_flav)    == list(t2.stats.dec_flav)
            assert list(t1.stats.prod_flav)   == list(t2.stats.prod_flav)
            assert list(t1.stats.eta)         == list(t2.stats.eta)
            assert list(t1.stats.weights)     == list(t2.stats.weights)
            assert list(t1.stats.all_weights) == list(t2.stats.all_weights)
            assert list(t1.stats.all_B_ID)    == list(t2.stats.all_B_ID)
            assert list(t1.stats.all_eta)     == list(t2.stats.all_eta)
            assert list(t1.stats.all_dec)     == list(t2.stats.all_dec)

    def same_values(taggers):
        for t1, t2 in itertools.combinations(taggers, 2):
            assert t1.stats.avg_eta == t2.stats.avg_eta
            assert t1.stats.N       == t2.stats.N
            assert t1.stats.Nw      == t2.stats.Nw
            assert t1.stats.Neff    == t2.stats.Neff
            assert t1.stats.Nt      == t2.stats.Nt

    df = pd.DataFrame({
        "eta"    : [0.2, 0.3, 0.4],
        "dec"    : [-1, 0, 1],
        "B_ID"   : [-521, 0, -521],
        "weight" : [0.3, 0.2, 0.7],
        "tau"    : [0.01, 0.02, 0.03],
        "tauerr" : [0.01, 0.02, 0.03],
    })
    mode = "Bd"
    name = "test1"

    try:
        t_list = ft.Tagger(name      = name,
                           eta_data  = list(df.eta),
                           dec_data  = list(df.dec),
                           B_ID      = list(df.B_ID),
                           tau_ps    = list(df.tau),
                           tauerr_ps = list(df.tauerr),
                           mode      = mode,
                           weight    = list(df.weight))
    except Exception as e:
        pytest.fail("List init failed")
        print(e.message)

    try:
        t_array = ft.Tagger(name      = name,
                            eta_data  = np.array(df.eta),
                            dec_data  = np.array(df.dec),
                            B_ID      = np.array(df.B_ID),
                            tau_ps    = np.array(df.tau),
                            tauerr_ps = np.array(df.tauerr),
                            mode      = mode,
                            weight    = np.array(df.weight))
    except Exception as e:
        pytest.fail("Array init failed")
        print(e.message)

    try:
        t_df = ft.Tagger(name      = name,
                         eta_data  = df.eta,
                         dec_data  = df.dec,
                         B_ID      = df.B_ID,
                         tau_ps    = df.tau,
                         tauerr_ps = df.tauerr,
                         mode      = mode,
                         weight    = df.weight)
    except Exception as e:
        pytest.fail("DataFrame init failed")
        print(e.message)

    # Test whether tagger data is pandas series and whether it is the same in all cases
    is_series(t_list)
    is_series(t_array)
    is_series(t_df)
    data_match([t_list, t_array, t_df])
    same_values([t_list, t_array, t_df])


def TagDataEquals(d1, d2):
    if d1 is None and d2 is None:
        return True
    equal = True
    equal &= d1.all_eta.equals(d2.all_eta)
    equal &= d1.all_dec.equals(d2.all_dec)
    equal &= d1.all_B_ID.equals(d2.all_B_ID)
    equal &= d1.tagged.equals(d2.tagged)
    equal &= d1.dec.equals(d2.dec)
    equal &= d1.dec_flav.equals(d2.dec_flav)
    equal &= d1.prod_flav.equals(d2.prod_flav)
    equal &= d1.eta.equals(d2.eta)
    equal &= d1.avg_eta == d2.avg_eta
    equal &= d1.weights.equals(d2.weights)
    equal &= d1.all_weights.equals(d2.all_weights)
    equal &= d1.correct_tags.equals(d2.correct_tags)
    equal &= d1.wrong_tags.equals(d2.wrong_tags)

    equal &= d1.N     == d2.N
    equal &= d1.Nt    == d2.Nt
    equal &= d1.Nw    == d2.Nw
    equal &= d1.Neff  == d2.Neff
    equal &= d1.Nwt   == d2.Nwt
    equal &= d1.Ns    == d2.Ns
    equal &= d1.Nts   == d2.Nts
    equal &= d1.Nws   == d2.Nws
    equal &= d1.Neffs == d2.Neffs
    equal &= d1.Nwts  == d2.Nwts
    return equal


def test_tagdata_equality():
    """ Test equality operator """
    td_ref = ft.TaggingData(eta_data  = [0.2, 0.1, 0.5],
                            dec_data  = [1, -1, 0],
                            ID        = [521, -521, 0],
                            tau       = None,
                            tauerr    = None,
                            weights   = [0.1, 0.2, 0.3],
                            selection = [True, True, True])

    td_clone      = deepcopy(td_ref)
    td_clone_fake = deepcopy(td_ref)

    assert id(td_clone) != id(td_ref)
    assert id(td_clone) != id(td_clone_fake)

    td_clone_fake.all_eta[1] *= 1.001

    assert TagDataEquals(td_ref, td_clone)
    assert not TagDataEquals(td_ref, td_clone_fake)


def test_tagdata_values():
    """ Test whether tagging statistics are determined as expected """
    dec_true     = pd.Series([1, 0, -1, 1, -1, 0, 0, 1, 0, -1], dtype=np.int32)
    eta_true     = pd.Series([0.1, 0.2, 0.3, 0.4, 0.3, 0.4, 0.2, 0.2, 0.3, 0.05])
    absid        = 521
    ID_true      = pd.Series(absid * np.array([1, 1, 1, -1, -1, 1, -1, 1, 1, -1]), dtype=np.int32)
    decay_flav   = ID_true // absid
    prod_flav    = decay_flav.copy()
    selection    = pd.Series([True, True, True, True, False, False, True, False, True, False])
    weights_true = pd.Series([0.3, 0.8, 0.2, 0.7, 1.2, 1.6, 0.2, 0.1, 0.7, 1.0])
    tag          = dec_true != 0
    tag_sel      = (dec_true != 0) & selection

    td = ft.TaggingData(eta_data = eta_true,
                        dec_data = dec_true,
                        ID       = ID_true,
                        tau      = None,
                        tauerr   = None,
                        weights  = weights_true,
                        selection = selection)

    # Basic data
    assert td.all_eta.equals(eta_true)
    assert td.all_dec.equals(dec_true)
    assert td.all_B_ID.equals(ID_true)
    assert td.selected.equals(selection)
    assert td.weights.equals(weights_true[tag_sel])

    # Basic memory safety (make sure data has been copied)
    assert id(td.all_eta)     != id(eta_true)
    assert id(td.all_dec)     != id(dec_true)
    assert id(td.all_B_ID)    != id(ID_true)
    assert id(td.all_weights) != id(weights_true)

    # overflow flags
    assert all(~td.overflow)
    assert all(~td.underflow)
    assert td.noverflow == 0

    # Higher level data
    assert td.tagged.equals(tag)
    assert td.weights.equals(weights_true[tag_sel])
    assert td.tagged_sel.equals(tag_sel)
    assert td.dec.equals(dec_true[tag_sel])
    assert td.dec_flav.equals(decay_flav[tag_sel])
    assert td.prod_flav.equals(prod_flav[tag_sel])
    assert td.eta.equals(eta_true[tag_sel])
    assert np.isclose(td.avg_eta, np.average(eta_true[tag_sel], weights=weights_true[tag_sel]))

    # Yields
    assert td.N  == len(eta_true)
    assert td.Ns == selection.sum()
    assert td.Nt == tag.sum()
    assert td.Nts == tag_sel.sum()
    assert np.isclose(td.Nw, np.sum(weights_true))
    assert np.isclose(td.Nwt, np.sum(weights_true[tag]))
    assert np.isclose(td.Nws, np.sum(weights_true[selection]))
    assert np.isclose(td.Nwts, np.sum(weights_true[tag_sel]))
    assert np.isclose(td.Neff, np.sum(weights_true) ** 2 / np.sum(weights_true**2))
    assert np.isclose(td.Neffs, np.sum(weights_true[selection]) ** 2 / np.sum(weights_true[selection]**2))

    # tag decision correctness
    assert td.correct_tags.equals(dec_true[tag_sel] == prod_flav[tag_sel])
    assert td.wrong_tags.equals(dec_true[tag_sel] != prod_flav[tag_sel])


def test_tagdata_constness_printing():
    """ Test whether printing functions change tagger statistics.
        That would be a bug
    """
    df = pd.DataFrame({
        "eta"    : [0.2, 0.5, 0.1],
        "dec"    : [-1, 0, 1],
        "B_ID"   : [-521, 521, 521],
        "tau"    : [0.01, 0.02, 0.03],
        "tauerr" : [0.003, 0.002, 0.001],
        "weight" : [0.3, 0.2, 0.7]
    })

    t1 = ft.Tagger(name      = "Test1",
                   eta_data  = df.eta,
                   dec_data  = df.dec,
                   B_ID      = df.B_ID,
                   mode      = "Bd",
                   tau_ps    = df.tau,
                   tauerr_ps = df.tauerr,
                   weight    = df.weight)
    t2 = ft.Tagger(name      = "Test2",
                   eta_data  = df.eta * 0.99,
                   dec_data  = -df.dec,
                   B_ID      = -df.B_ID,
                   mode      = "Bu",
                   tau_ps    = df.tau * 1.002,
                   tauerr_ps = df.tauerr * 0.99,
                   weight    = df.weight * 1.01)

    def print_stuff(t1, t2, calib):
        reference_data_1 = deepcopy(t1.stats)
        reference_data_2 = deepcopy(t2.stats)
        reference_cdata_1 = deepcopy(t1.cstats)
        reference_cdata_2 = deepcopy(t2.cstats)

        taggers = [t1, t2]

        ft.print_tagger_correlation(taggers, "all")
        ft.print_tagger_performances(taggers, calibrated=calib)
        ft.print_tagger_statistics(taggers, calibrated=calib)

        assert TagDataEquals(t1.stats, reference_data_1)
        assert TagDataEquals(t2.stats, reference_data_2)

        assert TagDataEquals(t1.cstats, reference_cdata_1)
        assert TagDataEquals(t2.cstats, reference_cdata_2)

    print_stuff(t1, t2, False)

    # pretend after calibration
    t1.cstats = deepcopy(t1.stats)
    t2.cstats = deepcopy(t2.stats)

    t1.params_nominal = np.array([0, 1, 0, 1])
    t2.params_nominal = np.array([0, 1, 0, 1])
    t1.params_uncerts = np.array([0.1, 0.1, 0.1, 0.1])
    t2.params_uncerts = np.array([0.1, 0.1, 0.1, 0.1])
    fake_cov = np.array([[0.01, 0, 0, 0], [0, 0.01, 0, 0], [0, 0, 0.01, 0], [0, 0, 0, 0.01]])
    t1.minimizer = FakeMinimizer(fake_cov)
    t2.minimizer = FakeMinimizer(fake_cov)

    t1._calibrated = True
    t2._calibrated = True
    print_stuff(t1, t2, True)


def test_tagdata_constness_perf():
    """ Test whether performance estimators change tagger statistics.
        That would be a bug
    """
    df = pd.DataFrame({
        "eta"    : [0.2, 0.5, 0.1],
        "dec"    : [-1, 0, 1],
        "B_ID"   : [-521, 521, 521],
        "tau"    : [0.01, 0.02, 0.03],
        "tauerr" : [0.003, 0.002, 0.001],
        "weight" : [0.3, 0.2, 0.7]
    })

    t = ft.Tagger(name      = "Test1",
                  eta_data  = df.eta,
                  dec_data  = df.dec,
                  B_ID      = df.B_ID,
                  mode      = "Bd",
                  tau_ps    = df.tau,
                  tauerr_ps = df.tauerr,
                  weight    = df.weight)

    reference_data = deepcopy(t.stats)

    ft.perf.mean_mistag(t, calibrated=False, selected=True)
    assert TagDataEquals(reference_data, t.stats)

    ft.perf.tagging_rate(t, calibrated=False, selected=True)
    assert TagDataEquals(reference_data, t.stats)

    ft.perf.tagging_power(t, calibrated=False, selected=True)
    assert TagDataEquals(reference_data, t.stats)

    t.params_nominal = np.array([0, 1, 0, 1])
    t.params_uncerts = np.array([0.1, 0.1, 0.1, 0.1])
    fake_cov = np.array([[0.01, 0, 0, 0], [0, 0.01, 0, 0], [0, 0, 0.01, 0], [0, 0, 0, 0.01]])
    t.minimizer = FakeMinimizer(fake_cov)
    t.cstats = deepcopy(t.stats)

    t._calibrated = True
    ft.perf.tagging_power(t, calibrated=True, selected=True)
    assert TagDataEquals(reference_data, t.stats)


def test_link_functions():
    """ Test link function derivatives numerically """
    mistag   = ft.link.mistag
    logit    = ft.link.logit
    rlogit   = ft.link.rlogit
    probit   = ft.link.probit
    rprobit  = ft.link.rprobit
    cauchit  = ft.link.cauchit
    rcauchit = ft.link.rcauchit

    x = np.linspace(-5, 5, 10000)

    def derivative_test(func):
        link  = func.L(x)
        dlink = func.DL(x)

        dlink_num = (link[2:] - link[:-2]) / (20 / 10000)

        plt.figure(figsize=(8, 6))
        plt.title(func.__name__)
        plt.plot(x, link)
        plt.plot(x, dlink)
        plt.plot(x[1:-1], dlink_num)

        if not os.path.exists("tests/testplots"):
            os.mkdir("tests/testplots")
        plt.savefig("tests/testplots/" + func.__name__ + "_D.pdf")

        if func.__name__ == "mistag":
            return
        assert np.max(np.abs(dlink[1:-1] - dlink_num)) < 0.001

    def inverse_test(func):
        link = func.L(x)
        linkInv = func.InvL(x)

        plt.figure(figsize=(8, 6))
        plt.title(func.__name__)
        plt.plot([-10, 10], [-10, 10], 'k--')
        plt.plot(x, link)
        plt.plot(x, linkInv)
        plt.xlim(-5, 5)
        plt.ylim(-5, 5)
        plt.savefig("tests/" + func.__name__ + "_Inv.pdf")

    derivative_test(mistag)
    derivative_test(logit)
    derivative_test(rlogit)
    derivative_test(probit)
    derivative_test(rprobit)
    derivative_test(cauchit)
    derivative_test(rcauchit)

    inverse_test(mistag)
    inverse_test(logit)
    inverse_test(rlogit)
    inverse_test(probit)
    inverse_test(rprobit)
    inverse_test(cauchit)
    inverse_test(rcauchit)


def test_convolution_at():
    # Test fast convolution algorithm for compliance to scipy.signal.convolve
    np.random.seed(3098750432)
    from scipy import signal

    for i in range(1000):
        arr1 = np.random.randint(-10, 10, np.random.randint(1, 128, 1))
        arr2 = np.random.randint(-10, 10, np.random.randint(1, 128, 1))

        reference = signal.convolve(arr1, arr2, mode="same")
        values    = np.array([ft.resolution_model.convolution_at(arr1, arr2, j) for j in range(len(arr1))])

        assert np.array_equal(reference, values)


def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    import sys
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size


def test_Tagger_frees_memory():
    # Test whether del causes memory to be freed
    N = 100000
    df = pd.DataFrame({
        "eta"    : np.random.uniform(0, 0.5, N),
        "dec"    : np.random.choice([-1, 0, 1], N),
        "B_ID"   : np.random.choice([-521, 0, 521], N),
        "tau"    : np.random.uniform(0, 0.01, N),
        "tauerr" : np.random.uniform(0, 0.001, N),
        "weight" : np.random.uniform(0, 1, N)
    })

    t = ft.Tagger(name      = "test",
                  eta_data  = df.eta,
                  dec_data  = df.dec,
                  B_ID      = df.B_ID,
                  mode      = "Bd",
                  tau_ps    = df.tau,
                  tauerr_ps = df.tauerr,
                  weight    = df.weight)

    taggersize = get_size(t)  # sys.getsizeof(t)
    print("Tagsize in mem", taggersize)

    t.destroy()

    taggersize = get_size(t)  # sys.getsizeof(t)
    print("Tagsize after in mem", taggersize)

    # Some couple of thousand bytes from tagger attributes are not destroyed
    assert taggersize < 10000


def test_TaggerCollection_frees_memory():
    # Test whether del causes memory to be freed
    N = 100000
    df = pd.DataFrame({
        "eta"    : np.random.uniform(0, 0.5, N),
        "dec"    : np.random.choice([-1, 0, 1], N),
        "B_ID"   : np.random.choice([-521, 0, 521], N),
        "tau"    : np.random.uniform(0, 0.01, N),
        "tauerr" : np.random.uniform(0, 0.001, N),
        "weight" : np.random.uniform(0, 1, N)
    })

    tc = ft.TaggerCollection()
    tc.create_tagger(name      = "test1",
                     eta_data  = df.eta,
                     dec_data  = df.dec,
                     B_ID      = df.B_ID,
                     mode      = "Bd",
                     tau_ps    = df.tau,
                     tauerr_ps = df.tauerr,
                     weight    = df.weight)
    tc.create_tagger(name      = "test2",
                     eta_data  = df.eta,
                     dec_data  = df.dec,
                     B_ID      = df.B_ID,
                     mode      = "Bd",
                     tau_ps    = df.tau,
                     tauerr_ps = df.tauerr,
                     weight    = df.weight)

    taggersize = get_size(tc)  # sys.getsizeof(t)
    print("Tagsize in mem", taggersize)

    tc.destroy()

    taggersize = get_size(tc)  # sys.getsizeof(t)
    print("Tagsize after in mem", taggersize)

    # Some couple of thousand bytes from tagger attributes are not destroyed
    assert taggersize < 10000, taggersize


def test_combination():
    from lhcb_ftcalib.combination import combine_taggers

    decs = []
    for d1 in [-1, 1, 0]:
        for d2 in [-1, 1, 0]:
            for d3 in [-1, 1, 0]:
                decs.append(np.array([d1, d2, d3]))

    omegas = []
    for w1 in [0.4, 0.2, 0.5]:
        for w2 in [0.2, 0.4, 0.5]:
            for w3 in [0.4, 0.5, 0.2]:
                omegas.append(np.array([w1, w2, w3]))

    assert len(decs) == len(omegas)
    cdec, comega = combine_taggers(decs, omegas)

    print(np.array(decs))
    print(np.array(omegas))
    print(cdec)
    print(comega)
    assert len(cdec) == len(comega)
    assert len(cdec) == len(decs)

    for i in range(len(cdec)):
        # Do values make sense
        assert cdec[i] in [1, -1, 0]
        assert comega[i] >= 0 and comega[i] <= 0.5
