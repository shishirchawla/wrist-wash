import numpy as np
import scipy

########################################################
# Utility functions for extracting features            #
########################################################
# Mean
def mean(data):
  return data.mean(0)

# Standard deviation
def stddev(data):
  return data.std(0)

# Kurtosis
def kurtosis(data):
  return scipy.stats.kurtosis(data)

# Skew
def skew(data):
  return scipy.stats.skew(data)

# ECDF
def ecdf(data, components=10):
    #
    #   rep = ecdfRep(data, components)
    #
    #   Estimate ecdf-representation according to
    #     Hammerla, Nils Y., et al. "On preserving statistical characteristics of
    #     accelerometry data using their empirical cumulative distribution."
    #     ISWC. ACM, 2013.
    #
    #   Input:
    #       data        Nxd     Input data (rows = samples).
    #       components  int     Number of components to extract per axis.
    #
    #   Output:
    #       rep         Mx1     Data representation with M = d*components+d
    #                           elements.
    #
    #   Nils Hammerla '15
    #
    m = data.mean(0)
    data = np.sort(data, axis=0)
    data = data[np.int32(np.around(np.linspace(0,data.shape[0]-1,num=components))),:]
    data = data.flatten(1)
    return np.hstack((data, m))

