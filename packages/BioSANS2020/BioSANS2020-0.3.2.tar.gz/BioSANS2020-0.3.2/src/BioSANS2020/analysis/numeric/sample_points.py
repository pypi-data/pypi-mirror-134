# import sys
# import os
# sys.path.append(os.path.abspath("BioSANS2020"))

"""
This module interpoltaes nsamp points from the trajectory.
"""

from numpy import linspace, interp


def sample_points(edata, nsamp=50000):
    """This function takes edata which is composed of numerical data and
    their labels and returns interpolated points.
    Args:
        edata : two dimensional array of data & labels (data, label).
                data is a 3D array where each row are the individual
                trajectories. Each trajectory is a 2D numpy array where
                the first column is time and the remaining columns are
                the corresponding components.
        nsamp : number of points to sample from data
    Returns:
        sdata : interpolated data points with sdata[0] is time and the
                remaining rows are interpolated data that corresponds to
                the time in sdata[0]
        label_name : labels
    """

    data, label_name = edata
    end_time = round(data[0][:, 0][-1])
    time = linspace(0, end_time, nsamp)
    sdata = [time]
    for ddrow in data:
        drow = []
        n_count = ddrow.shape[1]
        for i_index in range(1, n_count):
            y_interpolated = interp(time, ddrow[:, 0], ddrow[:, i_index])
            drow.append(y_interpolated)
        sdata.append(drow)
    return (sdata, label_name)
