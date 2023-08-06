import numpy as _np
from .consts import *


def gamma2GeV(gamma):
    n_pts = _np.size(gamma)
    if n_pts > 1:
        for i, val in enumerate(gamma):
            gamma[i] = gamma2GeV(val)
        return gamma
    else:
        gamma = _np.float(gamma)
        return gamma*electron_mc2_gev


def GeV2gamma(E):
    if _np.size(E) == 1:
        E = _np.float(E)
    else:
        E = _np.array(E, dtype='float')
    return E/electron_mc2_gev


def GeV2joule(E):
    return eV2joule(E) * 1e9


def eV2joule(E):
    if _np.size(E) == 1:
        E = _np.float(E)
    else:
        E = _np.array(E, dtype='float')

    return - E * e
