import numpy as np
cimport numpy as np
cimport cython

from libc.math cimport exp, log


DTYPE_FLOAT = np.double
ctypedef np.double_t DTYPE_FLOAT_t

DTYPE_INT = np.int
ctypedef np.int_t DTYPE_INT_t


#cdef extern from "math.h":
#    double log(double x) nogil
#    double exp(double x) nogil


@cython.boundscheck(False)
def sai_loop_1(np.ndarray[DTYPE_FLOAT_t, ndim=1] sini,
               np.ndarray[DTYPE_FLOAT_t, ndim=1] fc,
               np.ndarray[DTYPE_FLOAT_t, ndim=1] sc,
               np.ndarray[DTYPE_FLOAT_t, ndim=1] wp,
               np.ndarray[DTYPE_FLOAT_t, ndim=1] beta,
               np.ndarray[DTYPE_FLOAT_t, ndim=1] mu,
               np.ndarray[DTYPE_FLOAT_t, ndim=1] nu,
               np.ndarray[DTYPE_FLOAT_t, ndim=1] nuw,
               np.ndarray[DTYPE_FLOAT_t, ndim=1] tfc,
               np.ndarray[DTYPE_FLOAT_t, ndim=1] tsc,
               np.ndarray[DTYPE_FLOAT_t, ndim=1] twp):
    cdef unsigned int n_nodes = sini.size
    cdef unsigned int i

    for i in range(n_nodes):
        if sini[i] >= fc[i]:
            tfc[i] = (
              (1. / (beta[i] * (mu[i] - nu[i]))) *
              (beta[i] * (fc[i] - sini[i]) +
               log((nu[i] - mu[i] +
                    mu[i] * exp(beta[i] * (sini[i] - fc[i]))) / nu[i])))
            tsc[i] = ((fc[i] - sc[i]) / nu[i]) + tfc[i]
            twp[i] = (((sc[i] - wp[i]) / (nu[i] - nuw[i])) *
                      log(nu[i] / nuw[i]) + tsc[i])
