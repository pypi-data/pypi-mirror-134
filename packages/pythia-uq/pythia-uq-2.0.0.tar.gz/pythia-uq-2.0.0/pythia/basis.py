""" Assemble sparse univariate and multivariate basis polynomials.

Build univariate or multivariate normalized basis polynomials depending on
the domain and distribution (and other degrees of freedom) of the parameter(s).

Currently supported are the following distribution types:
    - uniform
    - normal
    - Gamma
    - Beta
"""
import numpy as np
import scipy.integrate
import scipy.special
import pythia as pt


def univariate_basis(params, degList):
    """ Assemble a univariate polynomial basis.

    Set polynomial basis up to deg for each parameter in `params` according to
    the parameter distribution and area of definition.

    Parameters
    ----------
    params : list of `pythia.parameter.Parameter`
        Parameters to compute univariate basis function for.
    degList : array_like
        Max. degrees of univariate polynomials for each parameter.

    Returns
    -------
    basis : list of list of functions
        List of normalized univariate polynomials w.r.t. parameter domain and
        distribution up to specified degree for each parameter in `params`.
    """
    basis = [None]*len(params)
    distDict = pt.misc.distributionDict()
    paramPDF = pt.density.paramPDF(params)
    for jj, param in enumerate(params):
        # Set the polynomial basis with corresponding area of support and
        # proper normalization.
        if param.distribution in distDict['uniform']:
            polynomials = normalize_polynomial(
                paramPDF[jj],
                set_legendre_basis(param, degList[jj]),
                param
            )
        elif param.distribution in distDict['normal']:
            polynomials = normalize_polynomial(
                paramPDF[jj],
                set_hermite_basis(param, degList[jj]),
                param
            )
        elif param.distribution in distDict['gamma']:
            polynomials = normalize_polynomial(
                paramPDF[jj],
                set_laguerre_basis(param, degList[jj]),
                param
            )
        elif param.distribution in distDict['beta']:
            polynomials = normalize_polynomial(
                paramPDF[jj],
                set_jacobi_basis(param, degList[jj]),
                param
            )
        else:
            text = 'Unsupported distribution "{}" for {}'.format(
                param.distribution, param.name
            )
            raise ValueError(text)

        basis[jj] = polynomials

    return basis


def multivariate_basis(paramBasis, mdx, partial=None):
    """ Assemble multivariate polynomial basis.

    Set the (partial derivative of the) multivariate (product) polynomial basis
    functions.

    Parameters
    ----------
    paramBasis : list of list of callable
        Univariate basis functions for parameters. Is called by
        `paramBasis[paramIdx][deg]()`.
    mdx : array_like
        Array of multiindices for multivariate basis functions.
    partial : list of int
        Number of partial derivatives for each dimension. Length is same as
        `paramBasis`.

    Returns
    -------
    pcBasis : list of functions
        List of normalized multivariate polynomials w.r.t. parameter domain and
        distribution and univariate degrees as specified in `mdx`.
    """
    if partial is not None:
        assert len(partial) == mdx.shape[1]
    pcBasis = [None]*mdx.shape[0]
    for jj, alpha in enumerate(mdx):
        def fun(x, alpha=alpha):
            if not 0 < x.ndim < 3:
                raise ValueError('Wrong ndim: {}'.format(x.ndim))
            if x.ndim == 1:
                x.shape = 1, -1
            if partial is None:
                basis = [paramBasis[k][a_k] for k, a_k in enumerate(alpha)]
            else:
                basis = [paramBasis[k][a_k].deriv(partial[k])
                         for k, a_k in enumerate(alpha)]
            return np.prod(
                [basis[k](x[:, k]) for k, _ in enumerate(alpha)],
                axis=0)
        pcBasis[jj] = fun
    return pcBasis


def normalize_polynomial(weight, p_list, param):
    """ Normalize orthogonal polynomials.

    Normalize a polynomial of an orthogonal system with respect to the scalar
    product

    .. math::
        a(u,v)_\\mathrm{pdf} = \\int u(p) v(p) \\mathrm{pdf}(p) \\mathrm{d}p.

    The normalized polynomial :math:`\\phi_j` for any given polynomial
    :math:`P_j` is given by :math:`\\phi_j = P_j / \\sqrt{c_j}`
    for the constant
    :math:`c_j = \\int \\mathrm{pdf}(p) * P_j(p)^2 \\mathrm{d}p`.

    Parameters
    ----------
    weight : callable
        Probability density function.
    p_list : list of `numpy.polynomial.Polynomial`
        Polynomials to normalize w.r.t. weight.
    param : `pythia.parameter.Parameter`
        Parameter used for distribution and domain information.

    Returns
    -------
    list of function
        List of normalized univariate polynomials.
    """
    distDict = pt.misc.distributionDict()
    c = [None]*len(p_list)
    for j, p in enumerate(p_list):
        if param.distribution in distDict["normal"]:
            c[j] = float(np.math.factorial(j))
        else:
            def fun(x): return weight(x)*p(x)**2
            c[j], _ = scipy.integrate.quad(
                fun, param.domain[0], param.domain[1])
    return [p/np.sqrt(c[j]) for j, p in enumerate(p_list)]


def set_legendre_basis(param, deg):
    """ Generate list of the Legendre Polynomials.

    Generate the Legendre Polynomials up to certain degree on the interval
    specified by the parameter.

    Parameters
    ----------
    param : `pythia.parameters.Parameter`
        Parameter for basis function. Needs to be uniformly distributed.
    deg : int
        Maximum degree for polynomials.

    Returns
    -------
    list of function
        Legendre polynomials up to (including) degree specified in `deg`.
    """
    return [np.polynomial.legendre.Legendre([0]*j+[1], param.domain)
            for j in range(deg+1)]


def set_hermite_basis(param, deg):
    """ Generate list of probabilists Hermite polynomials.

    Generate the Hermite Polynomials up to certain degree according to the
    mean and variance of the specified parameter.

    Parameters
    ----------
    param : `pythia.parameters.Parameter`
        Parameter for basis function. Needs to be normal distributed.
    deg : int
        Maximum degree for polynomials.

    Returns
    -------
    list of function
        Probabilists Hermite polynomials up to (including) degree specified
        in `deg`.
    """
    p_list = []
    mean, std = param.mean, np.sqrt(param.variance)
    b, a = 1/np.sqrt(2)/std, -mean/std/np.sqrt(2)
    shift = np.polynomial.polynomial.Polynomial([a, b])
    for j in range(deg+1):
        p = np.polynomial.hermite.Hermite([0]*j+[1])
        p_list.append(2**(-j/2)*p(shift))
    return p_list


def set_jacobi_basis(param, deg):
    """ Generate list of Jacobi polynomials.

    Generate the Jacobi Polynomials up to certain degree on the interval
    and DoFs specified by the parameter.

    Parameters
    ----------
    param : `pythia.parameters.Parameter`
        Parameter for basis function. Needs to be Beta-distributed.
    deg : int
        Maximum degree for polynomials.

    Returns
    -------
    list of function
        Jacobi polynomials up to (including) degree specified in `deg`.
    """
    p_list = [np.polynomial.polynomial.Polynomial(1)]

    a = pt.misc.shiftCoord(0, [-1, 1], param.domain)
    b = pt.misc.shiftCoord(1, [-1, 1], param.domain) - a
    shift = np.polynomial.polynomial.Polynomial([a, b])

    for j in range(1, deg+1):
        roots, _ = scipy.special.roots_jacobi(j, param.beta-1, param.alpha-1)
        coeff = np.polynomial.polynomial.polyfromroots(shift(roots))
        p = np.polynomial.polynomial.Polynomial(coeff)
        p_list.append(p)
    return p_list


def set_laguerre_basis(param, deg):
    """ Generate list of Leguerre polynomials.

    Generate the generalized Laguerre polynomials up to certain degree on
    the interval and DoFs specified by the parameter.

    Parameters
    ----------
    param : `pythia.parameters.Parameter`
        Parameter for basis function. Needs to be Gamma-distributed.
    deg : int
        Maximum degree for polynomials.

    Returns
    -------
    list of function
        Laguerre polynomials up to (including) degree specified in `deg`.
    """
    p_list = [np.polynomial.polynomial.Polynomial(1)]

    shift = np.polynomial.polynomial.Polynomial(
        [param.domain[0], 1/param.beta]
    )

    for j in range(1, deg+1):
        roots, _ = scipy.special.roots_genlaguerre(j, param.alpha-1)
        coeff = np.polynomial.polynomial.polyfromroots(shift(roots))
        p = np.polynomial.polynomial.Polynomial(coeff)
        p_list.append(p)
    return p_list


if __name__ == "__main__":
    pass
