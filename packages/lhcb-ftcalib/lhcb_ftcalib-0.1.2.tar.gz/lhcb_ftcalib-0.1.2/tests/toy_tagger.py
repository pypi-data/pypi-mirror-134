import os
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def gaussian_mistag(N, dist="normal", mean=0.25):
    if dist == "normal":
        return np.clip(np.random.normal(loc=mean, scale=0.05, size=N), 0, 0.5)


def distribution_mistag(tagdec, dist="OSMuon"):
    # Draw random mistag values from pre-sampled distributions

    def smear(distr, binwidth):
        # Add noise to sampled values so that they are uniformly distributed between bins
        N = len(distr)
        smear = np.random.uniform(-binwidth / 2, binwidth / 2, size=N)
        distr += smear
        distr[distr > 0.5] -= 0.5
        return distr

    taghists = pickle.load(open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "tagger_distributions.dict"), "rb"))
    Npos = np.sum(tagdec == 1)
    Nneg = np.sum(tagdec == -1)

    histbins = taghists["nbins"]
    histcenters = taghists["centers"]
    dist_pos = taghists[dist][1]["bins"]
    dist_neg = taghists[dist][-1]["bins"]
    p_density_pos = dist_pos / (2 * histbins)
    p_density_neg = dist_neg / (2 * histbins)

    eta = np.zeros(len(tagdec))
    eta[tagdec == +1] = smear(np.random.choice(histcenters, size=Npos, p=p_density_pos), 0.5 / histbins)
    eta[tagdec == -1] = smear(np.random.choice(histcenters, size=Nneg, p=p_density_neg), 0.5 / histbins)
    return eta


def decay_time_generator(chunk, lifetime):
    # Returns decay time distribution with arctan accepance model
    while True:
        tau = np.random.exponential(scale = 1.0 / lifetime, size=chunk)
        tau_choose  = np.random.uniform(0, 1, chunk)
        tau = tau[tau_choose < 2 * np.arctan(2 * tau) / np.pi]
        yield tau


def toy_data(N, calib, params, osc, tagger_types, life=1.52, DM=0.5065, DG=0, Aprod=0):
    """ Toy data generator """
    if osc:
        # Generate decay time
        tau_gen = decay_time_generator(N, life)
        tau = next(tau_gen)
        while len(tau) < N:
            tau = np.append(tau, next(decay_time_generator(N, life)))
        tau = tau[:N]
    
    # Start with prod == dec
    toydata = pd.DataFrame({
        "eventNumber" : np.arange(N),
        "TOY_PROD"    : np.ones(N, dtype=np.int32),
        "TOY_DECAY"   : np.ones(N, dtype=np.int32),
    })
    toydata.TOY_PROD.loc[N // 2:] *= -1
    toydata.TOY_DECAY.loc[N // 2:] *= -1

    if osc:
        # Oscillate mesons by inverting prod if oscillation is likely
        # This way, there is a time dependence between tag decision and production flavour
        toydata["TAU"] = tau
        Amix = np.cos(DM * toydata.TAU) / np.cosh(0.5 * DG * toydata.TAU)
        osc_prob = 0.5 * (1 - Amix)
        rand_thresh = np.random.uniform(0, 1, N)
        has_oscillated = rand_thresh < osc_prob
        toydata.loc[has_oscillated, "TOY_PROD"] *= -1
        toydata["OSC"] = has_oscillated

    # Generate the mistag distribution from stored histograms
    for t, tparams in enumerate(params):
        name = f"TOY{t}"
        toydata.eval(f"{name}_DEC = TOY_PROD", inplace=True)
        toydata[f"{name}_OMEGA"] = distribution_mistag(toydata[f"{name}_DEC"], dist=tagger_types[t])

    # Determine raw mistag from calibration function and simulate imperfect tagging
    for t, tparams in enumerate(params):
        name = f"TOY{t}"
        average_omega = np.mean(toydata[f"{name}_OMEGA"])

        # Compute tagging decision from omega, adjust DEC to match OMEGA
        rand_thresh = np.random.uniform(0, 1, N)
        toydata.loc[rand_thresh < toydata[f"{name}_OMEGA"], f"{name}_DEC"] *= -1

        # Compute true inverse omegas to get eta distributions
        inv_prec = 1000
        eta_lin = np.linspace(0, 0.5, inv_prec)
        # Reconstruct average eta which is unknown since calibration is
        # nonlinear, but: average_eta effectively shifts the mistag
        # distribution on eta axis.  Therefore, if we shift the omega distribution
        # so that it is centered at 0, we can measure the mean average eta shift
        # the calibration is applying to the eta distribution like this:
        # <eta>' = < omega^-1(omega - <omega>, 0) >
        # Then, when we shift the omega distribution back by <omega> we get
        # <eta> = <eta>' + <omega>
        # For less extreme/flavour asymmetric calibrations this seems to work sufficiently well

        omega_prime_lineshape = 0.5 * (calib.eval(tparams, eta_lin - average_omega, np.ones(inv_prec), 0) + calib.eval(tparams, eta_lin - average_omega, -np.ones(inv_prec), 0))
        average_etaprime = np.mean(np.interp(toydata[toydata["TOY_DECAY"] == +1][f"{name}_OMEGA"] - average_omega, omega_prime_lineshape, eta_lin - average_omega))
        average_eta = average_etaprime + average_omega

        omegaP_lineshape = calib.eval(tparams, eta_lin,  np.ones(inv_prec), average_eta)
        omegaM_lineshape = calib.eval(tparams, eta_lin, -np.ones(inv_prec), average_eta)
        toydata.loc[toydata["TOY_DECAY"] == +1, f"{name}_ETA"] = np.interp(toydata[toydata["TOY_DECAY"] == +1][f"{name}_OMEGA"], omegaP_lineshape, eta_lin)
        toydata.loc[toydata["TOY_DECAY"] == -1, f"{name}_ETA"] = np.interp(toydata[toydata["TOY_DECAY"] == -1][f"{name}_OMEGA"], omegaM_lineshape, eta_lin)

    # Shuffle
    toydata = toydata.sample(frac=1)

    return toydata
