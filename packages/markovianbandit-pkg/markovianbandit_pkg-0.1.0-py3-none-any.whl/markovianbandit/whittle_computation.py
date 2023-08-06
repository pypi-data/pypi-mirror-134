import numpy as np
import scipy.linalg
from numba import jit

def initialize_X_from_update(P0, P1, discount, X, pi):
    """
    Compute Delta*A_inv as defined in Algorithm 3 of the paper
    and store the product in matrix X
    """
    dim = P0.shape[0]
    i0 = 0 # state having null bias in non-discounted case
    mat_pol = np.copy(P1)
    for i, a in enumerate(pi):
        if a: continue
        else: mat_pol[i, :] = P0[i, :]
    Delta = P1 - P0
    if discount < 1.0:
        mat_pol *= discount
    else:
        mat_pol[:, i0] = -1.0
        mat_pol[i0, i0] = 0.0
        Delta[:, i0] = 0.0
    A = np.eye(dim, dtype=np.double) - mat_pol
    X[:,:] = scipy.linalg.solve(A.transpose(), Delta.transpose(), overwrite_a=True, overwrite_b=True, check_finite=False).transpose()


def find_mu_star(y, z, current_mu, delta, discount, atol):
    """
    Find the smallest
    """
    mu_star_k = current_mu
    next_sigma = -1
    mu_i_k = (delta + discount*(z - y*current_mu))/(1.0-discount*y)
    valid_idx = np.where( (mu_i_k > current_mu + atol) ) [0]
    if len(valid_idx)>0:
        argmin = mu_i_k[valid_idx].argmin()
        return valid_idx[argmin], mu_i_k[valid_idx[argmin]]
    else:
        return -1, current_mu

@jit
def compute_V_and_update_W(W, sigma, discount, X, k, check_indexability=True, k0=0):
    n = X.shape[0]
    V = np.copy(X[:, sigma])
    if check_indexability:
        for l in range(k0+1, k):
            c = V[n-l]
            for i in range(n):
                V[i] = V[i] - c * W[l-1, i]
        c = 1.0 + discount * V[n-k]
        for i in range(n):
            V[i] /= c
    else:
        for l in range(k0+1, k):
            c = V[n-l]
            for i in range(n-l+1):
                V[i] = V[i] - c * W[l-1, i]
        c = 1.0 + discount * V[n-k]
        for i in range(n-k):
            V[i] /= c
    W[k-1] = discount * V
    return V

#@profile
def compute_whittle_indices(P0, P1, R0, R1, discount=1, check_indexability=True, verbose=False, atol=1e-12, number_of_updates='2n**0.1'):
    """
    Implementation of Algorithm 3 of the paper
    Test whether the problem is indexable
    and compute Whittle indices when the problem is indexable
    The indices are computed in increasing order

    Args:
    - P0, P1: transition matrix for rest and activate actions respectively
    - R0, R1: reward vector for rest and activate actions respectively
    - discount: discount factor
    - check_indexability: if True check whether the problem is indexable or not
    - number_of_updates: (default = '2n**0.1'): number of time that X^{k} is recomputed from scratch.
    """
    dim = P0.shape[0]
    assert P0.shape == P1.shape
    assert R0.shape == R1.shape
    assert R0.shape[0] == dim

    is_indexable = True
    pi = np.ones(dim, dtype=np.double)
    sorted_sigmas = np.arange(dim)
    idx_in_sorted = np.arange(dim)
    whittle_idx = np.empty(dim, dtype=np.double)
    X = np.empty((dim, dim), dtype=np.double, order='C')
    sorted_X = np.empty((dim, dim), dtype=np.double, order='C')
    W = np.empty((dim-1,dim), dtype=np.double, order='C')
    k0 = 0
    if number_of_updates == '2n**0.1':
        number_of_updates = int(2*dim**0.1)
    frequency_of_update = dim / max(1, number_of_updates)

    initialize_X_from_update(P0, P1, discount, X, pi)
    y = -X.dot(pi)
    z = X.dot(R1)
    delta = R1 - R0
    whittle_idx = (delta + discount*z)/(1.0 - discount*y)
    argmin = np.argmin(whittle_idx)
    sigma = sorted_sigmas[argmin]
    z -= whittle_idx[sigma]*y

    if verbose: print('       ', end='')
    for k in range(1, dim):
        if verbose: print('\b\b\b\b\b\b\b{:7}'.format(k), end='', flush=True)
        """
        1. We sort the states so that the 'non visited' states are the first "dim-k"
           To do so, we exchange only one column of all matrices. 
        """
        tmp_s, idx_sigma = sorted_sigmas[dim-k], idx_in_sorted[sigma]
        idx_in_sorted[tmp_s], idx_in_sorted[sigma] = idx_in_sorted[sigma], idx_in_sorted[tmp_s]
        sorted_sigmas[dim-k], sorted_sigmas[idx_sigma] = sorted_sigmas[idx_sigma], sorted_sigmas[dim-k]

        X[dim-k, :], X[idx_sigma, :] = X[idx_sigma, :], np.copy(X[dim-k, :])
        W[:k-1, dim-k], W[:k-1, idx_sigma] = W[:k-1, idx_sigma], np.copy(W[:k-1, dim-k])

        delta[dim-k], delta[idx_sigma] = delta[idx_sigma], delta[dim-k]
        y[dim-k], y[idx_sigma] = y[idx_sigma], y[dim-k]
        z[dim-k], z[idx_sigma] = z[idx_sigma], z[dim-k]

        """
        2. If needed, we re-compute the matrix "X". This should not be done too often. 
        """
        if k > k0 + frequency_of_update:
            initialize_X_from_update(P0, P1, discount, X, pi)
            for i in range(dim):
                sorted_X[i] = np.copy(X[sorted_sigmas[i]])
            X = np.copy(sorted_X)
            k0 = k-1
        pi[sigma] = 0

        """
        3. We perform the recursive operations to compute X, y and z.
        """
        X[:, sigma] = compute_V_and_update_W(W, sigma, discount, X, k, check_indexability, k0)
        y += (1.0 - discount*y[dim-k])*X[:, sigma]
        argmin, mu_star_k = find_mu_star(y[0:dim-k], z[0:dim-k], whittle_idx[sigma], delta[0:dim-k], discount, atol)
        next_sigma = sorted_sigmas[argmin]
        whittle_idx[next_sigma] = mu_star_k
        z += (mu_star_k-whittle_idx[sigma])*y

        """
        4. If needed, we test if we violate the indexability condition. 
        """
        if check_indexability and is_indexable:
            if ((delta + discount*z > mu_star_k + atol)[dim-k:]).any():
                is_indexable = False
        sigma = next_sigma
    if verbose: print('\b\b\b\b\b\b\b', end='')
    return is_indexable, whittle_idx
