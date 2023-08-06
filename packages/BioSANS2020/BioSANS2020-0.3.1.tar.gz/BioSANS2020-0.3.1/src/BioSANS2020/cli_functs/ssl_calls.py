# import sys
# import os
# sys.path.append(os.path.abspath("BioSANS2020"))

"""
                       This is the ssl_calls module

This module interacts with BioSSL.py by fulfilling its requests to pro-
vide a console interface that supports some features of BioSANS.

The following is the list of function for this module:

1. load_data_traj
2. calc_average_conc_at_tend
3. calc_covariance
4. calc_covariance_per_traj
5. calc_covariance_bootsrap
6. prob_density_calc_wtime
7. prob_density_calc_tslice
8. prob_density_calc

"""

import numpy as np
import matplotlib.pyplot as plt
from BioSANS2020.analysis.numeric.sample_points import sample_points


def load_data_traj(file_name):
    """This function loads trajectory data from a tab delimited file.
    The first column in the file is time, the remaining columns are
    species or components. All sampled trajectories are concatenated
    in the file.
    Args:
        file_name : name of trajectory file generated in BioSANS
                    simulations (either deterministic or stochastic).
    Return:
        current_data : two dimensional array of [data, slabels].
                       slabels are the names in the header of file_name.
                       data is a list of trajectory data w/o header

    """
    with open(file_name, "r") as ffile:
        data = []
        ddvar = []
        row1 = str(ffile.readline()).strip()
        slabels = row1.split("\t")[1:]
        for row in ffile:
            cols = [float(x) for x in row.split("\t")]
            if cols[0] == 0.0 and len(ddvar) > 0:
                data.append(np.array(ddvar))
                ddvar = []
            ddvar.append(cols)
        data.append(np.array(ddvar))
    current_data = (data, slabels)
    return current_data


def calc_average_conc_at_tend(edata, points=100):
    """This function calculates the average or mean of edata[0] using
    the last number of points in the trajectory. If the simulation is
    long enought, this is the steady state mean concentration.
    Args:
        edata : two dimensional array of data & labels (data, label).
                data is a 3D array where each row are the individual
                trajectories. Each trajectory is a 2D numpy array where
                the first column is time and the remaining columns are
                the corresponding components.
        points : number of data points to slice at end of trajectory
    """
    data, slabels = edata
    nlen = len(data)
    ddm = 0
    for i in range(1, nlen):
        ddvar = data[i][-points:, 1:]
        ddm = ddm + ddvar

    ddm = np.mean(ddm / (nlen - 1), 0)
    dlen = len(slabels)
    print("\nSpecies Concentration\n")
    for i in range(dlen):
        if str(ddm[i]) not in {"None", "nan", "0.0"}:
            print(slabels[i].ljust(50) + " = " + str(ddm[i]))


def calc_covariance(edata, points=100):
    """This function calculates the covariance of edata[0] and prints
    the result in a console.
    Args:
        edata : two dimensional array of data & labels (data, label).
                data is a 3D array where each row are the individual
                trajectories. Each trajectory is a 2D numpy array where
                the first column is time and the remaining columns are
                the corresponding components.
        points : last number of points considered in covariance
                 calculation from -points to the end of array
                 or equivalent to [-points:] slice.
    """
    data, slabels = edata
    nlen = len(data)
    ddm = 0
    for i in range(1, nlen):
        ddvar = data[i][-points:, 1:]
        ddm = ddm + ddvar

    ddm = np.mean(ddm / (nlen - 1), 0)

    vvar = 0
    dlen = len(slabels)
    for k in range(1, nlen):
        ddvar = data[k][-points:, 1:] - ddm
        ddd = np.zeros((dlen, dlen))
        for i in range(dlen):
            for j in range(dlen):
                ddd[i, j] = np.mean(ddvar[:, i] * ddvar[:, j])
        vvar = vvar + ddd
    vvar = vvar / (nlen - 1)

    print("covariance\n")
    for i in range(dlen):
        for j in range(i, dlen):
            if str(vvar[i, j]) not in {"None", "nan", "0.0"}:
                label = slabels[i] + " and " + slabels[j]
                print(label.ljust(50) + " = " + str(vvar[i, j]))

    vvv = np.zeros((dlen, dlen))
    print("\ncorrelation\n")
    for i in range(dlen):
        for j in range(i, dlen):
            if str(vvar[i, j]) not in {"None", "nan", "0.0"}:
                vvv[i, j] = vvar[i, j] / np.sqrt(vvar[i, i] * vvar[j, j])
                label = slabels[i] + " and " + slabels[j]
                print(label.ljust(50) + " = " + str(vvv[i, j]))

    ffvar = 0
    cvcaps = 0
    for i in range(nlen):
        ddvar = 0
        ddvar = ddvar + (data[i][-points:, 1:] - ddm)**2
        ffvar = ffvar + np.mean(ddvar, 0) / ddm
        cvcaps = cvcaps + np.mean(np.sqrt(ddvar), 0) / ddm
    ffvar = ffvar / (nlen - 1)
    cvcaps = cvcaps / (nlen - 1)
    print("\nFano Factor\n")
    for i in range(dlen):
        if str(ffvar[i]) not in {"None", "nan", "0.0"}:
            print(slabels[i].ljust(50) + " = " + str(ffvar[i]))

    print("\nCoefficient of variation\n")
    for i in range(dlen):
        if str(cvcaps[i]) not in {"None", "nan", "0.0"}:
            print(slabels[i].ljust(50) + " = " + str(cvcaps[i]))


def calc_covariance_per_traj(edata, points=100, fname="", mname=""):
    """This function calculates the covariance of edata[0] per rows,
    prints the result in a console, and plots data into image.
    Args:
        edata : two dimensional array of data & labels (data, label).
                data is a 3D array where each row are the individual
                trajectories. Each trajectory is a 2D numpy array where
                the first column is time and the remaining columns are
                the corresponding components.
        points : last number of points considered in covariance
         calculation from -points to the end of array ([-points:] slice)
        fname : prepended name to plots fname_mname*
        mname : prepended name to plots fname_mname*
    """
    data, slabels = edata
    nlen = len(data)
    ddm = 0
    for i in range(1, nlen):
        ddvar = data[i][-points:, 1:]
        ddm = ddm + ddvar

    ddm = np.mean(ddm / (nlen - 1), 0)

    vvar = []
    ffvar = []
    cvlcase = []
    dlen = len(slabels)
    for k in range(1, nlen):
        ddvar = data[k][-points:, 1:] - ddm
        ddd = np.zeros((dlen, dlen))
        fff = np.zeros(dlen)
        cvv = np.zeros(dlen)
        for i in range(dlen):
            for j in range(dlen):
                ddd[i, j] = np.mean(ddvar[:, i] * ddvar[:, j])
            fff[i] = ddd[i, i] / ddm[i]
            cvv[i] = np.sqrt(ddd[i, i]) / ddm[i]
        vvar.append(ddd)
        ffvar.append(fff)
        cvlcase.append(cvv)
    vvar = np.array(vvar)
    ffvar = np.array(ffvar)
    cvlcase = np.array(cvlcase)
    mvv = np.mean(vvar, axis=0)
    svv = np.std(vvar, axis=0)
    mff = np.mean(ffvar, axis=0)
    sff = np.std(ffvar, axis=0)
    mcv = np.mean(cvlcase, axis=0)
    scv = np.std(cvlcase, axis=0)
    print("\ncovariance\n")
    for i in range(dlen):
        for j in range(i, dlen):
            if str(mvv[i, j]) not in {"None", "nan", "0.0"}:
                label = slabels[i] + " and " + slabels[j]
                print(label.ljust(50) + " = " +
                      str(mvv[i, j]), "std =", svv[i, j])

    plt.figure(figsize=(9.68, 3.95))
    plt.xlabel("covariance(P)")
    plt.ylabel("prob")
    plt.hist(vvar[:, dlen - 1, dlen - 1], bins=50,
             density=True, orientation='vertical')
    plt.axvline(mvv[dlen - 1, dlen - 1])
    plt.tight_layout()
    plt.savefig(fname + "_" + mname + "_covariance(P).jpg")
    plt.close()

    print("\nFano Factor\n")
    for i in range(dlen):
        if str(mff[i]) not in {"None", "nan", "0.0"}:
            print(slabels[i].ljust(50) + " = " + str(mff[i]), "std =", sff[i])

    plt.figure(figsize=(9.68, 3.95))
    plt.xlabel("Fano factor(P)")
    plt.ylabel("prob")
    plt.hist(ffvar[:, dlen - 1], bins=50, density=True, orientation='vertical')
    plt.axvline(mff[dlen - 1])
    plt.tight_layout()
    plt.savefig(fname + "_" + mname + "_Fano factor(P).jpg")
    plt.close()

    print("\nCoefficient of variation\n")
    for i in range(dlen):
        if str(mcv[i]) not in {"None", "nan", "0.0"}:
            print(slabels[i].ljust(50) + " = " + str(mcv[i]), "std =", scv[i])

    plt.figure(figsize=(9.68, 3.95))
    plt.xlabel("Coeff. of Var.(P)")
    plt.ylabel("prob")
    plt.hist(cvlcase[:, dlen - 1], bins=50, density=True,
             orientation='vertical')
    plt.axvline(mcv[dlen - 1])
    plt.tight_layout()
    plt.savefig(fname + "_" + mname + "_CoeffOfVar(P).jpg")
    plt.close()


def calc_covariance_bootsrap(
        edata, points=100, msamp=1000, fname="", mname=""):
    """This function calculates the covariance of edata[0] with sampling
    , prints the result in a console, and plots data into image.
    Args:
        edata : two dimensional array of data & labels (data, label).
                data is a 3D array where each row are the individual
                trajectories. Each trajectory is a 2D numpy array where
                the first column is time and the remaining columns are
                the corresponding components.
        points : last number of points considered in covariance
                 calculation from -points to the end of array
                 or equivalent to [-points:] slice.
        msamp : number of randomly chosen trajectories
        fname : prepended name to plots fname_mname*
        mname : prepended name to plots fname_mname*
    """
    data, slabels = edata
    nlen = len(data)
    bmvv = []
    bsvv = []
    bmff = []
    bsff = []
    bmcv = []
    bscv = []
    mlist = list(range(1, nlen))
    np.random.shuffle(mlist)
    for _ in range(1000):
        ddm = 0
        curr_list = np.random.choice(mlist, msamp)
        for i in curr_list:
            ddvar = data[i][-points:, 1:]
            ddm = ddm + ddvar

        ddm = np.mean(ddm / msamp, 0)

        vvar = []
        ffvar = []
        cvlcase = []
        dlen = len(slabels)
        for k in curr_list:
            ddvar = data[k][-points:, 1:] - ddm
            ddd = np.zeros((dlen, dlen))
            fff = np.zeros(dlen)
            cvv = np.zeros(dlen)
            for i in range(dlen):
                for j in range(dlen):
                    ddd[i, j] = np.mean(ddvar[:, i] * ddvar[:, j])
                fff[i] = ddd[i, i] / ddm[i]
                cvv[i] = np.sqrt(ddd[i, i]) / ddm[i]
            vvar.append(ddd)
            ffvar.append(fff)
            cvlcase.append(cvv)
        vvar = np.array(vvar)
        ffvar = np.array(ffvar)
        cvlcase = np.array(cvlcase)
        mvv = np.mean(vvar, axis=0)
        svv = np.std(vvar, axis=0)
        mff = np.mean(ffvar, axis=0)
        sff = np.std(ffvar, axis=0)
        mcv = np.mean(cvlcase, axis=0)
        scv = np.std(cvlcase, axis=0)
        bmvv.append(mvv)
        bsvv.append(svv)
        bmff.append(mff)
        bsff.append(sff)
        bmcv.append(mcv)
        bscv.append(scv)

    bmvv = np.array(bmvv)
    bsvv = np.array(bsvv)
    bmff = np.array(bmff)
    bsff = np.array(bsff)
    bmcv = np.array(bmcv)
    bscv = np.array(bscv)

    mvv = np.mean(bmvv, axis=0)
    svv = np.std(bmvv, axis=0)
    mff = np.mean(bmff, axis=0)
    sff = np.std(bmff, axis=0)
    mcv = np.mean(bmcv, axis=0)
    scv = np.std(bmcv, axis=0)

    print("\ncovariance\n")
    for i in range(dlen):
        for j in range(i, dlen):
            if str(mvv[i, j]) not in {"None", "nan", "0.0"}:
                label = slabels[i] + " and " + slabels[j]
                print(label.ljust(50) + " = " +
                      str(mvv[i, j]), "std =", svv[i, j])

    plt.figure(figsize=(9.68, 3.95))
    plt.xlabel("covariance(P)")
    plt.ylabel("prob")
    plt.hist(bmvv[:, dlen - 1, dlen - 1], bins=50,
             density=True, orientation='vertical')
    plt.axvline(mvv[dlen - 1, dlen - 1])
    plt.tight_layout()
    plt.savefig(fname + "_" + mname + "_covariance(P)_bootsrap.jpg")
    plt.close()

    print("\nFano Factor\n")
    for i in range(dlen):
        if str(mff[i]) not in {"None", "nan", "0.0"}:
            print(slabels[i].ljust(50) + " = " + str(mff[i]), "std =", sff[i])

    plt.figure(figsize=(9.68, 3.95))
    plt.xlabel("Fano factor(P)")
    plt.ylabel("prob")
    plt.hist(bmff[:, dlen - 1], bins=50, density=True, orientation='vertical')
    plt.axvline(mff[dlen - 1])
    plt.tight_layout()
    plt.savefig(fname + "_" + mname + "_Fano factor(P)_bootsrap.jpg")
    plt.close()

    print("\nCoefficient of Variation\n")
    for i in range(dlen):
        if str(mcv[i]) not in {"None", "nan", "0.0"}:
            print(slabels[i].ljust(50) + " = " + str(mcv[i]), "std =", scv[i])

    plt.figure(figsize=(9.68, 3.95))
    plt.xlabel("Coeff. of Var.")
    plt.ylabel("prob")
    plt.hist(bmcv[:, dlen - 1], bins=50, density=True, orientation='vertical')
    plt.axvline(mcv[dlen - 1])
    plt.tight_layout()
    plt.savefig(fname + "_" + mname + "_CoeffofVar(P)_bootsrap.jpg")
    plt.close()


def prob_density_calc_wtime(edata, fname, mname):
    """This function calculates the probability density of edata[0] and
    returns a plot of the probability density with time.
    Args:
        edata : two dimensional array of data & labels (data, label).
                data is a 3D array where each row are the individual
                trajectories. Each trajectory is a 2D numpy array where
                the first column is time and the remaining columns are
                the corresponding components.
        fname : prepended name to plots fname_mname*
        mname : prepended name to plots fname_mname*
    """
    data, slabels = edata
    nlen = len(data)
    dlen = len(slabels)

    ddvar = data[0][:, 1:]
    ttime = data[0][:, 0].flatten()
    # tlen = len(ttime)
    for i in range(1, nlen):
        ddvar = np.concatenate((ddvar, data[i][:, 1:]), axis=0)
        ttime = np.concatenate((ttime, data[i][:, 0]))

    for j in range(dlen):
        ddd = ddvar[:, j].flatten()
        csq = int(np.sqrt(len(ddd)))
        zss, xss, yss = np.histogram2d(ttime, ddd, bins=(csq, csq))
        plt.figure(figsize=(9.68, 3.95))
        plt.xlabel("time")
        plt.ylabel("conc(" + slabels[j] + ")")
        delcon = int(np.max(zss) - np.min(zss)) / 500
        if slabels[j] == "P":
            plt.yscale('log')
        delcon = int(np.max(zss) - np.min(zss)) / 500
        try:
            cntr = plt.contour(xss[1:], yss[1:], zss.T,
                               list(range(int(np.min(zss)),
                                          int(np.max(zss)) + 1,
                                          int(delcon))
                                    ), cmap="Spectral_r")
        except:
            cntr = plt.contour(xss[1:], yss[1:], zss.T, 100, cmap="Spectral_r")
        fig = plt.gcf()
        fig.colorbar(cntr)
        plt.tight_layout()
        plt.savefig(
            fname +
            "_" +
            mname +
            "_" +
            slabels[j] +
            "_prob_density_wtime.jpg")
        plt.close()


def prob_density_calc_tslice(edata, bins=50, fname=""):
    """This function calculates the probability density of edata[0] per
    bins and returns a plot of the probability density.
    Args:
        edata : two dimensional array of data & labels (data, label).
                data is a 3D array where each row are the individual
                trajectories. Each trajectory is a 2D numpy array where
                the first column is time and the remaining columns are
                the corresponding components.
        bins : number of bins an entire trajectory will be discretized
        fname : name prepended to plot name
    """
    if len(edata[0]) != 3:
        ndata, slabels = sample_points(edata)
        time = ndata[0]
        nlen = len(ndata)
        dlen = len(slabels)

        ddd = [[] for x in range(dlen)]
        for k in range(1, nlen):
            ddvar = ndata[k]
            for j in range(dlen):
                ddd[j].append(ddvar[j])
        ddd = np.array(ddd)

        vvv = {}
        for i in range(dlen):
            for j in range(len(time)):
                vvv[(i, j)] = np.histogram(ddd[i][:, j], bins=bins)

        tlen = len(time)
        strt = int(tlen / 10)
        for i in range(dlen):
            lines = []
            fig = plt.figure(figsize=(9.68, 3.95))
            axf = fig.gca(projection='3d')
            for j in range(strt, tlen, int(tlen / 5)):
                xss = vvv[(i, j)][1][1:]
                yss = vvv[(i, j)][0]
                width = (xss[1] - xss[0])
                line = axf.bar(xss, yss, zs=time[j], zdir='x',
                               width=max(width, 0.8), alpha=1)
                lines.append(line)
            axf.set_xlabel('time')
            axf.set_ylabel("conc(" + slabels[i] + ")")
            axf.set_zlabel('freq')
            axf.view_init(elev=40, azim=-120)
            plt.savefig(fname + "_" + slabels[j] + "_prob_density_tslice.jpg")
            plt.close()


def prob_density_calc(edata, fname):
    """This function calculates the probability density of edata[0] and
    returns a plot of the probability density.
    Args:
        edata : two dimensional array of data & labels (data, label).
                data is a 3D array where each row are the individual
                trajectories. Each trajectory is a 2D numpy array where
                the first column is time and the remaining columns are
                the corresponding components.
        items : 3 item list of [canvas, scroll_x, scroll_y]
    """
    data, slabels = edata
    nlen = len(data)
    dlen = len(slabels)

    ddvar = data[0][:, 1:]
    for i in range(1, nlen):
        ddvar = np.concatenate((ddvar, data[i][:, 1:]), axis=0)

    for j in range(dlen):
        plt.figure(figsize=(9.68, 3.95))
        plt.xlabel("conc(" + slabels[j] + ")")
        plt.ylabel("Prob")
        ddd = ddvar[:, j]
        _ = plt.hist(ddd, bins=int(np.sqrt(len(ddd))),
                     density=True, orientation='vertical')
        plt.legend([slabels[j]])
        plt.xscale('log')
        plt.tight_layout()
        _ = plt.gcf()
        plt.savefig(fname + "_" + slabels[j] + "_prob_density.jpg")
        plt.close()
