from scipy.stats import norm, lognorm, expon, lomax, weibull_min, fisk
import numpy as np


def rvs_fn1(n):
    return norm.rvs(10, 1, size=n)


def rvs_fn2(n):
    return lognorm.rvs(1, 0, size=n)


def rvs_fn3(n):
    return np.random.exponential(size=n)


def rvs_fn4(n):
    return lomax.rvs(c=.9, size=n)


def rvs_fn5(n):
    return weibull_min.rvs(c=5, size=n)


def rvs_fn6(n):
    return fisk.rvs(c=.3, size=n)


def ppf_fn1(q):
    return norm.ppf(q, 10, 1)


def ppf_fn2(q):
    return lognorm.ppf(q, 1, 0)


def ppf_fn3(q):
    return expon.ppf(q)


def ppf_fn4(q):
    return lomax.ppf(q, c=.9)


def ppf_fn5(q):
    return weibull_min.ppf(q, c=5)


def ppf_fn6(q):
    return fisk.ppf(q, c=.3)


distributions_shelf = {
                        "Normal": (rvs_fn1, ppf_fn1),
                        "LogNormal": (rvs_fn2, ppf_fn2),
                        "Exponential": (rvs_fn3, ppf_fn3),
                        "Lomax": (rvs_fn4, ppf_fn4),
                        "Weibull": (rvs_fn5, ppf_fn5),
                        "LogLogistic": (rvs_fn6, ppf_fn6)
                       }
