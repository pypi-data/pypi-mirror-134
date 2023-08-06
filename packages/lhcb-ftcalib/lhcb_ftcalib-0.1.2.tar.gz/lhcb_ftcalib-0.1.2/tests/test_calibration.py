import os
import numpy as np
import uproot
from toy_tagger import toy_data
import lhcb_ftcalib as ft


def delete_file(F):
    if os.path.exists(F):
        os.remove(F)
        print("Removed", F)


def test_prepare_tests():
    if not os.path.exists("tests/calib"):
        os.mkdir("tests/calib")

    # Generate toy data for calibration testing
    if not os.path.exists("tests/calib/toy_data.root"):
        poly1 = ft.PolynomialCalibration(2, ft.link.mistag)
        toydata = toy_data(30000, poly1, [[0, 1, 0, 1],
                                          [0.01, 1.3, 0.01, 1],
                                          [0.01, 1, 0.01, 1.3]],
                                          tagger_types=["OSKaon", "SSPion", "OSMuon"],
                                          osc=False)

        File = uproot.recreate("tests/calib/toy_data.root")
        File["BU_TOY"] = toydata

        toydata = toy_data(30000, poly1, [[0, 1, 0, 1],
                                          [0.01, 1.3, 0.01, 1],
                                          [0.01, 1, 0.01, 1.3]],
                                          tagger_types=["OSKaon", "SSPion", "OSMuon"],
                                          osc=True)
        File["BD_TOY"] = toydata


def TagDataEquals(d1, d2):
    assert np.allclose(d1.all_eta, d2.all_eta)
    assert np.allclose(d1.all_dec, d2.all_dec)
    assert np.allclose(d1.all_B_ID, d2.all_B_ID)
    assert np.allclose(d1.tagged, d2.tagged)
    assert np.allclose(d1.dec, d2.dec)
    assert np.allclose(d1.dec_flav, d2.dec_flav)
    assert np.allclose(d1.prod_flav, d2.prod_flav)
    assert np.allclose(d1.eta, d2.eta)
    assert np.allclose(d1.avg_eta, d2.avg_eta)
    assert np.allclose(d1.weights, d2.weights)

    assert d1.N     == d2.N
    assert d1.Nt    == d2.Nt
    assert d1.Nw    == d2.Nw
    assert d1.Neff  == d2.Neff
    assert d1.Nwt   == d2.Nwt
    assert d1.Ns    == d2.Ns
    assert d1.Nts   == d2.Nts
    assert d1.Nws   == d2.Nws
    assert d1.Neffs == d2.Neffs
    assert d1.Nwts  == d2.Nwts


def compare_dataframe_to_file(filename, key, df):
    # Tests the content of a root file to a dataframe for equality within
    # rounding errors to make sure API and CLI give same results
    assert os.path.exists(filename)
    fdata = uproot.open(filename)[key].arrays(library="pd")
    for branch in fdata.columns.values:
        if branch in df:
            print(f"Comparing branch {branch} ...")
            b1 = np.array(fdata[branch])
            b2 = np.array(df[branch])
            if not all(np.isclose(b1, b2)):
                print("FAIL")
                print("CLI ", b1[b1 != b2])
                print("API ", b2[b1 != b2])
                raise AssertionError
            print("PASSED")


def test_run_calibrate_Bu():
    # Run CLI command without crashing, then do the same with the API and compare results
    # CLI
    testfile = "tests/calib/test_calibrate_Bu"
    delete_file(testfile + ".json")
    F = "tests/calib/toy_data.root"

    df = uproot.open(F)["BU_TOY"].arrays(["TOY0_ETA", "TOY1_ETA", "TOY2_ETA",
                                          "TOY0_DEC", "TOY1_DEC", "TOY2_DEC", "TOY_DECAY"], library="pd")
    tc = ft.TaggerCollection()
    tc.create_tagger("TOY0", df.TOY0_ETA, df.TOY0_DEC, B_ID=df.TOY_DECAY, mode="Bu")
    tc.create_tagger("TOY1", df.TOY1_ETA, df.TOY1_DEC, B_ID=df.TOY_DECAY, mode="Bu")
    tc.create_tagger("TOY2", df.TOY2_ETA, df.TOY2_DEC, B_ID=df.TOY_DECAY, mode="Bu")
    tc.calibrate()
    apidata = tc.get_dataframe(calibrated=True)

    delete_file(testfile + ".json")


def test_run_calibrate_combine_Bu():
    # Run CLI command without crashing, then do the same with the API and compare results
    # CLI
    testfile = "tests/calib/test_calibrate_combine_Bu"
    delete_file(testfile + ".json")
    F = "tests/calib/toy_data.root"

    df = uproot.open(F)["BU_TOY"].arrays(["TOY0_ETA", "TOY1_ETA", "TOY2_ETA",
                                          "TOY0_DEC", "TOY1_DEC", "TOY2_DEC", "TOY_DECAY"], library="pd")
    tc = ft.TaggerCollection()
    tc.create_tagger("TOY0", df.TOY0_ETA, df.TOY0_DEC, B_ID=df.TOY_DECAY, mode="Bu")
    tc.create_tagger("TOY1", df.TOY1_ETA, df.TOY1_DEC, B_ID=df.TOY_DECAY, mode="Bu")
    tc.create_tagger("TOY2", df.TOY2_ETA, df.TOY2_DEC, B_ID=df.TOY_DECAY, mode="Bu")
    tc.calibrate()
    apidata = tc.get_dataframe(calibrated=True)
    combination = tc.combine_taggers("Combination", calibrated=True)
    combdata = combination.get_dataframe(calibrated=False)
    for v in combdata.columns.values:
        apidata[v] = combdata[v]

    delete_file(testfile + ".json")


def test_run_calibrate_combine_calibrate_Bu():
    # Run CLI command without crashing, then do the same with the API and compare results
    # CLI
    testfile = "tests/calib/test_calibrate_combine_calibrate_Bu"
    delete_file(testfile + ".json")
    F = "tests/calib/toy_data.root"

    df = uproot.open(F)["BU_TOY"].arrays(["TOY0_ETA", "TOY1_ETA", "TOY2_ETA",
                                          "TOY0_DEC", "TOY1_DEC", "TOY2_DEC", "TOY_DECAY"], library="pd")
    tc = ft.TaggerCollection()
    tc.create_tagger("TOY0", df.TOY0_ETA, df.TOY0_DEC, B_ID=df.TOY_DECAY, mode="Bu")
    tc.create_tagger("TOY1", df.TOY1_ETA, df.TOY1_DEC, B_ID=df.TOY_DECAY, mode="Bu")
    tc.create_tagger("TOY2", df.TOY2_ETA, df.TOY2_DEC, B_ID=df.TOY_DECAY, mode="Bu")
    tc.calibrate()
    apidata = tc.get_dataframe(calibrated=True)
    combination = tc.combine_taggers("Combination", calibrated=True)
    combination.calibrate(ignore_eta_out_of_range=False)
    combdata = combination.get_dataframe(calibrated=False)
    combdata_calib = combination.get_dataframe(calibrated=True)
    for v in combdata.columns.values:
        apidata[v] = combdata[v]
    for v in combdata_calib.columns.values:
        apidata[v] = combdata_calib[v]

    delete_file(testfile + ".json")


def test_run_calibrate_Bd():
    # Run CLI command without crashing, then do the same with the API and compare results
    # CLI
    testfile = "tests/calib/test_calibrate_Bd"
    delete_file(testfile + ".json")
    F = "tests/calib/toy_data.root"

    df = uproot.open(F)["BD_TOY"].arrays(["TOY0_ETA", "TOY1_ETA", "TOY2_ETA",
                                          "TOY0_DEC", "TOY1_DEC", "TOY2_DEC", "TOY_DECAY", "TAU"], library="pd")
    tc = ft.TaggerCollection()
    tc.create_tagger("TOY0", df.TOY0_ETA, df.TOY0_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU)
    tc.create_tagger("TOY1", df.TOY1_ETA, df.TOY1_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU)
    tc.create_tagger("TOY2", df.TOY2_ETA, df.TOY2_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU)
    tc.calibrate()
    apidata = tc.get_dataframe()

    delete_file(testfile + ".json")


def test_run_calibrate_Bd_selection_vartype1():
    # Run CLI command without crashing, then do the same with the API and compare results
    # CLI
    testfile = "tests/calib/test_calibrate_Bd_sel_v1"
    delete_file(testfile + ".json")
    F = "tests/calib/toy_data.root"

    df = uproot.open(F)["BD_TOY"].arrays(["TOY0_ETA", "TOY1_ETA", "TOY2_ETA",
                                          "TOY0_DEC", "TOY1_DEC", "TOY2_DEC", "TOY_DECAY", "TAU"], library="pd")
    selection = df.TAU > 0.5
    tc = ft.TaggerCollection()
    tc.create_tagger("TOY0", df.TOY0_ETA, df.TOY0_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU, selection=selection)
    tc.create_tagger("TOY1", df.TOY1_ETA, df.TOY1_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU, selection=selection)
    tc.create_tagger("TOY2", df.TOY2_ETA, df.TOY2_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU, selection=selection)
    tc.calibrate()
    apidata = tc.get_dataframe()

    delete_file(testfile + ".json")


def test_run_calibrate_Bd_selection_vartype2():
    # Run CLI command without crashing, then do the same with the API and compare results
    # CLI
    # import pudb
    # pu.db
    testfile = "tests/calib/test_calibrate_Bd_sel_v2"
    delete_file(testfile + ".json")
    F = "tests/calib/toy_data.root"

    df = uproot.open(F)["BD_TOY"].arrays(["TOY0_ETA", "TOY1_ETA", "TOY2_ETA",
                                          "TOY0_DEC", "TOY1_DEC", "TOY2_DEC", "TOY_DECAY", "TAU", "eventNumber"], library="pd")
    selection = df.eventNumber % 2 == 0
    tc = ft.TaggerCollection()
    tc.create_tagger("TOY0", df.TOY0_ETA, df.TOY0_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU, selection=selection)
    tc.create_tagger("TOY1", df.TOY1_ETA, df.TOY1_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU, selection=selection)
    tc.create_tagger("TOY2", df.TOY2_ETA, df.TOY2_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU, selection=selection)
    tc.calibrate()
    apidata = tc.get_dataframe()

    delete_file(testfile + ".json")


def test_run_calibrate_combine_Bd():
    # Run CLI command without crashing, then do the same with the API and compare results
    # CLI
    testfile = "tests/calib/test_calibrate_combine_Bd"
    delete_file(testfile + ".json")
    F = "tests/calib/toy_data.root"

    df = uproot.open(F)["BD_TOY"].arrays(["TOY0_ETA", "TOY1_ETA", "TOY2_ETA",
                                          "TOY0_DEC", "TOY1_DEC", "TOY2_DEC", "TOY_DECAY", "TAU"], library="pd")
    tc = ft.TaggerCollection()
    tc.create_tagger("TOY0", df.TOY0_ETA, df.TOY0_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU)
    tc.create_tagger("TOY1", df.TOY1_ETA, df.TOY1_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU)
    tc.create_tagger("TOY2", df.TOY2_ETA, df.TOY2_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU)
    tc.calibrate()
    combination = tc.combine_taggers("Combination", calibrated=True)
    apidata = tc.get_dataframe(calibrated=True)
    combdata = combination.get_dataframe(calibrated=False)
    for v in combdata.columns.values:
        apidata[v] = combdata[v]

    delete_file(testfile + ".json")


def test_run_calibrate_combine_calibrate_Bd():
    # Run CLI command without crashing, then do the same with the API and compare results
    # CLI
    testfile = "tests/calib/test_calibrate_combine_calibrate_Bd"
    delete_file(testfile + ".json")
    F = "tests/calib/toy_data.root"

    df = uproot.open(F)["BD_TOY"].arrays(["TOY0_ETA", "TOY1_ETA", "TOY2_ETA",
                                          "TOY0_DEC", "TOY1_DEC", "TOY2_DEC", "TOY_DECAY", "TAU"], library="pd")
    tc = ft.TaggerCollection()
    tc.create_tagger("TOY0", df.TOY0_ETA, df.TOY0_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU)
    tc.create_tagger("TOY1", df.TOY1_ETA, df.TOY1_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU)
    tc.create_tagger("TOY2", df.TOY2_ETA, df.TOY2_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU)
    tc.calibrate()
    combination = tc.combine_taggers("Combination", calibrated=True)
    combination.calibrate()
    apidata = tc.get_dataframe(calibrated=True)
    combdata = combination.get_dataframe(calibrated=False)
    combdata_calib = combination.get_dataframe(calibrated=True)
    for v in combdata.columns.values:
        apidata[v] = combdata[v]
    for v in combdata_calib.columns.values:
        apidata[v] = combdata_calib[v]

    delete_file(testfile + ".json")


def test_run_calibrate_combine_calibrate_Bd_selection():
    # Run CLI command without crashing, then do the same with the API and compare results
    # CLI
    testfile = "tests/calib/test_calibrate_combine_calibrate_Bd_sel"
    delete_file(testfile + ".json")
    F = "tests/calib/toy_data.root"

    df = uproot.open(F)["BD_TOY"].arrays(["TOY0_ETA", "TOY1_ETA", "TOY2_ETA",
                                          "TOY0_DEC", "TOY1_DEC", "TOY2_DEC", "TOY_DECAY", "TAU", "eventNumber"], library="pd")

    selection = df.eventNumber % 2 == 0
    tc = ft.TaggerCollection()
    tc.create_tagger("TOY0", df.TOY0_ETA, df.TOY0_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU, selection=selection)
    tc.create_tagger("TOY1", df.TOY1_ETA, df.TOY1_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU, selection=selection)
    tc.create_tagger("TOY2", df.TOY2_ETA, df.TOY2_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU, selection=selection)
    tc.calibrate()
    combination = tc.combine_taggers("Combination", calibrated=True)
    combination.calibrate()
    apidata = tc.get_dataframe(calibrated=True)
    combdata = combination.get_dataframe(calibrated=False)
    combdata_calib = combination.get_dataframe(calibrated=True)
    for v in combdata.columns.values:
        apidata[v] = combdata[v]
    for v in combdata_calib.columns.values:
        apidata[v] = combdata_calib[v]

    delete_file(testfile + ".json")


def test_run_calibrate_save_load():
    # Run CLI command without crashing, then do the same with the API and compare results
    # CLI
    testfile = "tests/calib/test_calibrate_save_load"
    delete_file(testfile + ".json")
    calibfile = "tests/calib/test_calibration"
    delete_file(calibfile + ".json")
    F = "tests/calib/toy_data.root"

    df = uproot.open(F)["BD_TOY"].arrays(["TOY0_ETA", "TOY1_ETA", "TOY2_ETA",
                                          "TOY0_DEC", "TOY1_DEC", "TOY2_DEC", "TOY_DECAY", "TAU"], library="pd")
    tc = ft.TaggerCollection()
    tc.create_tagger("TOY0", df.TOY0_ETA, df.TOY0_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU)
    tc.create_tagger("TOY1", df.TOY1_ETA, df.TOY1_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU)
    tc.create_tagger("TOY2", df.TOY2_ETA, df.TOY2_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU)
    tc.calibrate()
    origdata = tc.get_dataframe(calibrated=True)

    ft.save_calibration(tc, title=calibfile + ".json")

    tc_flavour = ft.TargetTaggerCollection()
    tc_flavour.create_tagger("TOY0", df.TOY0_ETA, df.TOY0_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU)
    tc_flavour.create_tagger("TOY1", df.TOY1_ETA, df.TOY1_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU)
    tc_flavour.create_tagger("TOY2", df.TOY2_ETA, df.TOY2_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU)
    tc_flavour.load_calibrations(calibfile + ".json", style="flavour")
    tc_flavour.apply(ignore_delta=True)
    flavourdata = tc_flavour.get_dataframe(calibrated=True)

    # import pudb; pu.db
    # tc_flavour[0].get_fitparameters()

    tc_delta = ft.TargetTaggerCollection()
    tc_delta.create_tagger("TOY0", df.TOY0_ETA, df.TOY0_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU)
    tc_delta.create_tagger("TOY1", df.TOY1_ETA, df.TOY1_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU)
    tc_delta.create_tagger("TOY2", df.TOY2_ETA, df.TOY2_DEC, B_ID=df.TOY_DECAY, mode="Bd", tau_ps=df.TAU)
    tc_delta.load_calibrations(calibfile + ".json", style="delta")
    tc_delta.apply(ignore_delta=True)
    deltadata = tc_delta.get_dataframe(calibrated=True)

    for t in range(3):
        ft.printing.print_calibration_info(tc[t])
        ft.printing.print_calibration_info(tc_delta[t])
        ft.printing.print_calibration_info(tc_flavour[t])


    # Test calibration functions and tagging data
    for t in range(3):
        assert tc[t].func.npar == tc_delta[t].func.npar
        assert tc[t].func.npar == tc_flavour[t].func.npar
        assert tc[t].func.param_names == tc_delta[t].func.param_names
        assert tc[t].func.param_names == tc_flavour[t].func.param_names
        assert tc[t].func.param_names_delta == tc_delta[t].func.param_names_delta
        assert tc[t].func.param_names_delta == tc_flavour[t].func.param_names_delta
        assert tc[t].func.link == tc_delta[t].func.link
        assert tc[t].func.link == tc_flavour[t].func.link

        TagDataEquals(tc[t].stats, tc_flavour[t].stats)
        TagDataEquals(tc[t].stats, tc_delta[t].stats)

        TagDataEquals(tc[t].cstats, tc_delta[t].cstats)
        TagDataEquals(tc[t].cstats, tc_flavour[t].cstats)

    for t in range(3):
        assert np.allclose(tc[t].stats.eta, tc_flavour[t].stats.eta)
        assert np.allclose(tc[t].stats.eta, tc_delta[t].stats.eta)
        assert np.allclose(tc[t].stats.dec, tc_flavour[t].stats.dec)
        assert np.allclose(tc[t].stats.dec, tc_delta[t].stats.dec)

        # assert np.allclose(tc[t].cstats.eta, tc_flavour[t].cstats.eta)
        # assert np.allclose(tc[t].cstats.eta, tc_delta[t].cstats.eta)
        assert np.allclose(tc[t].cstats.dec, tc_flavour[t].cstats.dec)
        assert np.allclose(tc[t].cstats.dec, tc_delta[t].cstats.dec)

    print("Difference between delta and flavour:")
    print((deltadata - flavourdata).describe())
    print("Difference between orig and flavour:")
    print((origdata - flavourdata).describe())
    print("Difference between delta and orig:")
    print((deltadata - origdata).describe())

    assert all([np.allclose(deltadata[c], flavourdata[c]) for c in origdata.columns])
    assert all([np.allclose(origdata[c], flavourdata[c]) for c in origdata.columns])
    assert all([np.allclose(origdata[c], deltadata[c]) for c in origdata.columns])

    delete_file(calibfile + ".json")
    delete_file(testfile + ".json")
