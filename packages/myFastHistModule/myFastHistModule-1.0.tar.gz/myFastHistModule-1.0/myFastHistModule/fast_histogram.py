import numpy as np
import matplotlib.pyplot as plt

def fast_hist(X, bins_num):

    X_max = max(X)
    X_min = min(X)
    l = (X_max - X_min) / bins_num
    bins = np.arange(X_min, X_max, l)
    ans = np.zeros(bins_num)
    for val in X:
        ans[min(int((val - X_min) / l), bins_num - 1)] += 1
    return (np.array([int (x) for x in ans]), bins)