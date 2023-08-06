# distutils: extra_compile_args = -O2 -w
# distutils: include_dirs = pylds/
# cython: boundscheck = False, nonecheck = False, wraparound = False, cdivision = True

import numpy as np
from numpy.lib.stride_tricks import as_strided

cimport numpy as np
cimport cython
from libc.math cimport log, sqrt
from numpy.math cimport INFINITY, PI

from blas_lapack cimport dsymm, dcopy, dgemm, dpotrf, \
        dgemv, dpotrs, daxpy, dtrtrs, dsyrk, dtrmv, \
        dger, dnrm2, dpotri, copy_transpose, copy_upper_lower, ddot

# TODO instead of specializing last step in info filtering and rts, we could
# instead just pad the input J's and h's by zeroes


#################################
#  information-form operations  #
#################################

def kalman_info_filter(
    double[:,:] J_init, double[:] h_init,
    double[:,:,:] J_pair_11, double[:,:,:] J_pair_21, double[:,:,:] J_pair_22,
    double[:,:,:] J_node, double[:,:] h_node):

    # allocate temporaries and internals
    cdef int T = J_node.shape[0], n = J_node.shape[1]
    cdef int t

    cdef double[:,:] J_predict = np.copy(J_init)
    cdef double[:] h_predict = np.copy(h_init)

    cdef double[::1]   temp_n   = np.empty((n,), order='F')
    cdef double[::1,:] temp_nn  = np.empty((n,n),order='F')
    cdef double[::1,:] temp_nn2 = np.empty((n,n),order='F')

    # allocate output
    cdef double[:,:,::1] filtered_Js = np.empty((T,n,n))
    cdef double[:,::1] filtered_hs = np.empty((T,n))
    cdef double lognorm = 0.

    # run filter forwards
    for t in range(T-1):
        info_condition_on(
            J_predict, h_predict, J_node[t], h_node[t],
            filtered_Js[t], filtered_hs[t])
        lognorm += info_predict(
            filtered_Js[t], filtered_hs[t], J_pair_11[t], J_pair_21[t], J_pair_22[t],
            J_predict, h_predict,
            temp_n, temp_nn, temp_nn2)
    info_condition_on(
        J_predict, h_predict, J_node[T-1], h_node[T-1],
        filtered_Js[T-1], filtered_hs[T-1])
    lognorm += info_lognorm_copy(
        filtered_Js[T-1], filtered_hs[T-1], temp_n, temp_nn)

    return lognorm, np.asarray(filtered_Js), np.asarray(filtered_hs)


def info_E_step(
    double[:,::1] J_init, double[::1] h_init,
    double[:,:,:] J_pair_11, double[:,:,:] J_pair_21, double[:,:,:] J_pair_22,
    double[:,:,:] J_node, double[:,:] h_node):
    # NOTE: uses two-filter strategy

    # allocate temporaries and internals
    cdef int T = J_node.shape[0], n = J_node.shape[1]
    cdef int t

    cdef double[:,:,::1] filtered_Js = np.empty((T,n,n))
    cdef double[:,::1] filtered_hs = np.empty((T,n))
    cdef double[:,:,::1] predict_Js = np.empty((T,n,n))
    cdef double[:,::1] predict_hs = np.empty((T,n))

    cdef double[::1]   temp_n   = np.empty((n,), order='F')
    cdef double[::1,:] temp_nn  = np.empty((n,n),order='F')
    cdef double[::1,:] temp_nn2 = np.empty((n,n),order='F')

    # allocate output
    cdef double[:,::1] smoothed_mus = np.empty((T,n))
    cdef double[:,:,::1] smoothed_sigmas = np.empty((T,n,n))
    cdef double[:,:,::1] Cov_xxns = np.empty((T-1,n,n))  # 'n' for next
    cdef double lognorm = 0.

    # run filter forwards
    predict_Js[0,:,:] = J_init
    predict_hs[0,:] = h_init
    for t in range(T-1):
        info_condition_on(
            predict_Js[t], predict_hs[t], J_node[t], h_node[t],
            filtered_Js[t], filtered_hs[t])
        lognorm += info_predict(
            filtered_Js[t], filtered_hs[t], J_pair_11[t], J_pair_21[t], J_pair_22[t],
            predict_Js[t+1], predict_hs[t+1],
            temp_n, temp_nn, temp_nn2)
    info_condition_on(
        predict_Js[T-1], predict_hs[T-1], J_node[T-1], h_node[T-1],
        filtered_Js[T-1], filtered_hs[T-1])
    lognorm += info_lognorm_copy(
        filtered_Js[T-1], filtered_hs[T-1], temp_n, temp_nn)

    # run info-form rts update backwards
    # overwriting the filtered params with smoothed ones
    info_to_distn(
        filtered_Js[T-1], filtered_hs[T-1],
        smoothed_mus[T-1], smoothed_sigmas[T-1])
    for t in range(T-2,-1,-1):
        info_rts_backward_step(
            J_pair_11[t], J_pair_21[t], J_pair_22[t],
            predict_Js[t+1], filtered_Js[t], filtered_Js[t+1],  # filtered_Js[t] is mutated
            predict_hs[t+1], filtered_hs[t], filtered_hs[t+1],  # filtered_hs[t] is mutated
            smoothed_mus[t], smoothed_sigmas[t], Cov_xxns[t],
            temp_n, temp_nn, temp_nn2)

    return lognorm, np.asarray(smoothed_mus), np.asarray(smoothed_sigmas), np.asarray(Cov_xxns)


###########################
#  information-form util  #
###########################

cdef inline void info_condition_on(
    double[:,:] J1, double[:] h1,
    double[:,:] J2, double[:] h2,
    double[:,:] Jout, double[:] hout,
    ) nogil:
    cdef int n = J1.shape[0]
    cdef int i

    for i in range(n):
        hout[i] = h1[i] + h2[i]

    for i in range(n):
        for j in range(n):
            Jout[i,j] = J1[i,j] + J2[i,j]


cdef inline double info_predict(
    double[:,:] J, double[:] h, double[:,:] J11, double[:,:] J21, double[:,:] J22,
    double[:,:] Jpredict, double[:] hpredict,
    double[:] temp_n, double[:,:] temp_nn, double[:,:] temp_nn2,
    ) nogil:

    # NOTE: J21 is in C-major order, so BLAS and LAPACK function calls mark it as
    # transposed

    cdef int n = J.shape[0]
    cdef int nn = n*n
    cdef int inc = 1, info = 0
    cdef double one = 1., zero = 0., neg1 = -1., lognorm = 0.

    dcopy(&nn, &J[0,0], &inc, &temp_nn[0,0], &inc)
    daxpy(&nn, &one, &J11[0,0], &inc, &temp_nn[0,0], &inc)
    dcopy(&nn, &J22[0,0], &inc, &Jpredict[0,0], &inc)
    dcopy(&nn, &J21[0,0], &inc, &temp_nn2[0,0], &inc)
    dcopy(&n, &h[0], &inc, &temp_n[0], &inc)

    lognorm += info_lognorm(temp_nn, temp_n)  # mutates temp_n and temp_nn
    dtrtrs('L', 'T', 'N', &n, &inc, &temp_nn[0,0], &n, &temp_n[0], &n, &info)
    # NOTE: transpose because J21 is in C-major order
    dgemv('T', &n, &n, &neg1, &J21[0,0], &n, &temp_n[0], &inc, &zero, &hpredict[0], &inc)

    dtrtrs('L', 'N', 'N', &n, &n, &temp_nn[0,0], &n, &temp_nn2[0,0], &n, &info)
    # TODO this call aliases pointers, should really call dsyrk and copy lower to upper
    dgemm('T', 'N', &n, &n, &n, &neg1, &temp_nn2[0,0], &n, &temp_nn2[0,0], &n, &one, &Jpredict[0,0], &n)
    # dsyrk('L', 'T', &n, &n, &neg1, &temp_nn2[0,0], &n, &one, &Jpredict[0,0], &n)

    return lognorm


cdef inline double info_lognorm(double[:,:] J, double[:] h) nogil:
    # NOTE: mutates input to chol(J) and solve_triangular(chol(J),h), resp.

    cdef int n = J.shape[0]
    cdef int nn = n*n
    cdef int inc = 1, info = 0
    cdef double lognorm = 0.

    dpotrf('L', &n, &J[0,0], &n, &info)
    dtrtrs('L', 'N', 'N', &n, &inc, &J[0,0], &n, &h[0], &n, &info)

    lognorm += (1./2) * dnrm2(&n, &h[0], &inc)**2
    for i in range(n):
        lognorm -= log(J[i,i])
    lognorm += n/2. * log(2*PI)

    return lognorm


cdef inline double info_lognorm_copy(
    double[:,:] J, double[:] h,
    double[:] temp_n, double[:,:] temp_nn,
    ) nogil:
    cdef int n = J.shape[0]
    cdef int nn = n*n, inc = 1

    dcopy(&nn, &J[0,0], &inc, &temp_nn[0,0], &inc)
    dcopy(&n, &h[0], &inc, &temp_n[0], &inc)

    return info_lognorm(temp_nn, temp_n)


cdef inline void info_rts_backward_step(
    double[:,:] J11, double[:,:] J21, double[:,:] J22,
    double[:,:] Jpred_tp1, double[:,:] Jfilt_t, double[:,:] Jsmooth_tp1,  # Jfilt_t is mutated!
    double[:] hpred_tp1, double[:] hfilt_t, double[:] hsmooth_tp1,  # hfilt_t is mutated!
    double[:] mu_t, double[:,:] sigma_t, double[:,:] Cov_xnx,
    double[:] temp_n, double[:,:] temp_nn, double[:,:] temp_nn2,
    ) nogil:

    # NOTE: this function mutates Jfilt_t and hfilt_t to be Jsmooth_t and
    # hsmooth_t, respectively
    # NOTE: J21 is in C-major order, so BLAS and LAPACK function calls mark it as
    # transposed

    cdef int n = J11.shape[0]
    cdef int nn = n*n
    cdef int inc = 1, info = 0
    cdef double one = 1., zero = 0., neg1 = -1.

    dcopy(&nn, &Jsmooth_tp1[0,0], &inc, &temp_nn[0,0], &inc)
    daxpy(&nn, &neg1, &Jpred_tp1[0,0], &inc, &temp_nn[0,0], &inc)
    daxpy(&nn, &one, &J22[0,0], &inc, &temp_nn[0,0], &inc)
    copy_transpose(n, n, &J21[0,0], &temp_nn2[0,0])

    dpotrf('L', &n, &temp_nn[0,0], &n, &info)
    dtrtrs('L', 'N', 'N', &n, &n, &temp_nn[0,0], &n, &temp_nn2[0,0], &n, &info)
    daxpy(&nn, &one, &J11[0,0], &inc, &Jfilt_t[0,0], &inc)
    dgemm('T', 'N', &n, &n, &n, &neg1, &temp_nn2[0,0], &n, &temp_nn2[0,0], &n, &one, &Jfilt_t[0,0], &n)

    dcopy(&n, &hsmooth_tp1[0], &inc, &temp_n[0], &inc)
    daxpy(&n, &neg1, &hpred_tp1[0], &inc, &temp_n[0], &inc)
    dpotrs('L', &n, &inc, &temp_nn[0,0], &n, &temp_n[0], &n, &info)
    dgemv('N', &n, &n, &neg1, &J21[0,0], &n, &temp_n[0], &inc, &one, &hfilt_t[0], &inc)

    info_to_distn(Jfilt_t, hfilt_t, mu_t, sigma_t)

    dgemm('T', 'N', &n, &n, &n, &neg1, &J21[0,0], &n, &sigma_t[0,0], &n, &zero, &Cov_xnx[0,0], &n)
    dpotrs('L', &n, &n, &temp_nn[0,0], &n, &Cov_xnx[0,0], &n, &info)


cdef inline void info_to_distn(
    double[:,:] J, double[:] h, double[:] mu, double[:,:] Sigma,
    ) nogil:
    cdef int n = J.shape[0]
    cdef int nn = n*n
    cdef int inc = 1, info = 0
    cdef double zero = 0., one = 1.

    dcopy(&nn, &J[0,0], &inc, &Sigma[0,0], &inc)
    dpotrf('L', &n, &Sigma[0,0], &n, &info)
    dpotri('L', &n, &Sigma[0,0], &n, &info)
    copy_upper_lower(n, &Sigma[0,0])  # NOTE: 'L' in Fortran order, but upper for C order
    dgemv('N', &n, &n, &one, &Sigma[0,0], &n, &h[0], &inc, &zero, &mu[0], &inc)


###################
#  test bindings  #
###################

def info_predict_test(J,h,J11,J21,J22,Jpredict,hpredict):
    temp_n = np.random.randn(*h.shape)
    temp_nn = np.random.randn(*J.shape)
    temp_nn2 = np.random.randn(*J.shape)

    return info_predict(J,h,J11,J21,J22,Jpredict,hpredict,temp_n,temp_nn,temp_nn2)


def info_rts_test(
        J11, J21, J22, Jpred_tp1, Jfilt_t, Jsmooth_tp1, hpred_tp1, hfilt_t,
        hsmooth_tp1, mu_t, sigma_t, Cov_xnx):
    temp_n = np.random.randn(*mu_t.shape)
    temp_nn = np.random.randn(*sigma_t.shape)
    temp_nn2 = np.random.randn(*sigma_t.shape)

    info_rts_backward_step(
        J11, J21, J22, Jpred_tp1, Jfilt_t, Jsmooth_tp1,
        hpred_tp1, hfilt_t, hsmooth_tp1, mu_t, sigma_t, Cov_xnx,
        temp_n, temp_nn, temp_nn2)

