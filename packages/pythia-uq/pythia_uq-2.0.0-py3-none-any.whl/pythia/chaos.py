""" Sample-based computation of polynomial chaos expansion.

This module provides classes to compute the polynomial chaos approximation of
an unknown function given via input/output training data pairs via linear
least-squares regression.
"""
import numpy as np
import psutil
import pythia as pt


class PolynomialChaos(object):
    """ Computation of sparse polynomial chaos expansion.

    Parameters
    ----------
    params : dict/list of `pythia.parameter.RandomParameter`
        Parameter to specify random variables for chaos expansion.
    mdx : `pythia.index.PCMultiIndex`
        Multiindices of coefficients of the polynomial chaos expansion.
    regPoints : array_like
        Regression points for linar regression (Parameter realizations).
    weights : array_like
        Regression weights for `regPoints`.
    fEval : array_like
        Function evaluation of `regPoints` and `xVal`.
    xVal : array_like, optional
        Spacial/physical point of function evaluation.

    Other Parameters
    ----------------
    infoMatrix : array_like, optional
        Information matrix (Gramian) of the basis functions and samples.
    basisMat : array_like, optional
        Basis evaluation matrix of samples.
    regLength : int, default=0
        Number of regression points used in linear regression.
        Needs to be less or equal to length of mdx.
        Zero results in automatic choice of amount of sample points.
    paramPDF : list of function, optional
        List of univariate PDFs for each parameter.
    pdf : function, optional
        Multivariate PDF of parameters.
    paramBasis : list of list of function, optional
        Univariate basis functions for each parameter.
    basis : list of function, optional
        Multivariate basis functions as specified in `mdx`.
    coeff : array_like, optional
        PC coefficients.
    verbose : bool, default=False
        Makes PCE talk.
    """

    def __init__(self, params, mdx, regPoints, weights, fEval,
                 xVal=None, infoMatrix=None, basisMat=None, regLength=0,
                 paramPDF=None, pdf=None, paramBasis=None, basis=None,
                 coeff=None, verbose=False):
        """ Initiate the computation of the PC expansion of a function. """
        self._params = params
        if isinstance(self._params, dict):
            self._params = pt.misc.paramDictToList(params)
        assert isinstance(self._params, list)
        for param in self._params:
            assert isinstance(param, pt.parameter.RandomParameter)
        self._pDim = len(self._params)
        self._mdx = mdx
        assert isinstance(self._mdx, pt.index.PCMultiIndex)
        self._regPoints = regPoints
        assert self._regPoints.ndim == 2
        assert self._regPoints.shape[1] == len(self._params)
        self._weights = weights
        assert self._weights.ndim == 1
        assert self._weights.shape[0] == self._regPoints.shape[0]
        self._fEval = fEval
        assert self._fEval.ndim == 2
        assert self._fEval.shape[0] == self._regPoints.shape[0]
        self._fDim = self._fEval.shape[1]
        self._xVal = xVal
        if self._xVal is not None:
            assert self._xVal.ndim == 1
            self._xDim = self._xVal.shape[0]
        else:
            self._xDim = 0

        self._regLength = int(regLength)
        assert 0 <= self._regLength <= self._regPoints.shape[0]
        # Compute regression points for evalutation of PCE coefficients.
        if self._regLength == 0:
            self._regLength = pt.misc.wlsSamplingBound(self._mdx.count, c=2)

        self._infoMatrix = infoMatrix
        if self._infoMatrix is not None:
            assert self._infoMatrix.shape == (self._mdx.count,)*2
        self._basisMat = basisMat
        if self._basisMat is not None:
            assert self._basisMat.shape == (self._regLength, self._mdx.count)
        self._paramPDF, self._pdf = paramPDF, pdf
        self._paramBasis, self._basis = paramBasis, basis
        self._coeff = coeff
        if self._coeff is not None:
            assert self._coeff.shape == (self._mdx.count, self._fDim)

        self._verbose = verbose
        assert isinstance(self._verbose, bool)

        # Check parameters.
        self._checkParamAttributes(pt.misc.distributionDict())

        # Compute univariate and multivariate densities.
        if self._paramPDF is None:
            self._paramPDF = pt.density.paramPDF(self._params)
        if self._pdf is None:
            self._pdf = pt.density.multivariatePDF(self._paramPDF)

        # Compute univariate and multivariate orthonormal basis polynomials.
        if self._paramBasis is None:
            self._paramBasis = pt.basis.univariate_basis(
                self._params, self._mdx.maximum)
        if self._basis is None:
            self._basis = pt.basis.multivariate_basis(
                self._paramBasis, self._mdx.mdx)

        # Assemble information matrix.
        self._infoMatrix, self._basisMat, self._W = self._assembleMatrices(
            self._basis)

        # Compute coefficients for polynomial chaos expansion.
        if self._coeff is None:
            self._coeff = self._computePCECoefficients(
                self._infoMatrix, self._basisMat, self._W, self._fEval
            )

        # Compute mean and variance.
        self._mean = self._computeMean()
        self._var = self._computeVar()

        # Compute Sobol coefficients and total variance.
        self._sobolCoeff = self._computeSobolCoeff()

    @property
    def parameter(self):
        """ List of parameters. """
        return self._params

    @property
    def mdx(self):
        """ Multiindices object. """
        return self._mdx

    @property
    def regPoints(self):
        """ Parameter realization used for training. """
        return self._regPoints

    @property
    def weights(self):
        """ Regression weights. """
        return self._weights

    @property
    def fEval(self):
        """ Function evaluations used for training. """
        return self._fEval

    @property
    def xVal(self):
        """ Spatial component. """
        return self._xVal

    @property
    def regLength(self):
        """ Number of used training data to compute PC expansion. """
        return self._regLength

    @property
    def pDim(self):
        """ Number of random parameters. """
        return self._pDim

    @property
    def xDim(self):
        """ Spatial dimension. """
        return self._xDim

    @property
    def fDim(self):
        """ Image dimension of the function. """
        return self._fDim

    @property
    def paramPDF(self):
        """ List of univariate PDFs for each parameter. """
        return self._paramPDF

    @property
    def pdf(self):
        """ Multivariate PDF of parameters. """
        return self._pdf

    @property
    def paramBasis(self):
        """ List of univariate basis functions for each parameter. """
        return self._paramBasis

    @property
    def basis(self):
        """ Multivariate basis functions used for the PC expansion. """
        return self._basis

    @property
    def infoMatrix(self):
        """ Information matrix (unscaled Gramian) for the samples. """
        return self._infoMatrix

    @property
    def basisMat(self):
        """ Basis evaluation matrix :math:`P_j(y_i)`. """
        return self._basisMat

    @property
    def coeff(self):
        """ Coefficients of the PC expansion. """
        return self._coeff

    @property
    def mean(self):
        """ Mean of the PC expansion. """
        return self._mean

    @property
    def variance(self):
        """ Variance of the PC expansion. """
        return self._var

    @property
    def std(self):
        """ Standard deviation of the PC expansion. """
        return np.sqrt(self._var)

    @property
    def sobolCoeff(self):
        """ Approximated Sobol indices for the PC expansion. """
        return self._sobolCoeff

    def _computePCECoefficients(self, A, Psi, W, fEval):
        """ Compute PCE coefficients.

        Compute the PCE coefficients with linear regression. The coefficients
        are given by

        .. math::
            S = A^(-1) * \\Psi^T * W * F_\\mathrm{ex}

        where the information matrix :math:`A` is of full rank but may be ill
        conditioned.  :math:`F_\\mathrm{ex}` is an array containing the values
        of f evaluated at the required regression points. For more detail on
        the information matrix or :math:`\\Psi`, see function
        `assembleInformationMatrix()`.
        """

        if self._verbose:
            print('{}: Solve linear regression ...'.format(pt.misc.now()))

        # Apply a singular value decomposition to invert information matrix A.
        u, s, vh = np.linalg.svd(A)
        Ainv = np.dot(vh.T, np.dot(np.diag(1/s), u.T))
        W.shape = -1, 1
        S = np.linalg.multi_dot([Ainv, Psi.T, W*fEval[:self._regLength]])
        return S

    def _computeMean(self):
        """ Compute PCE mean.

        Compute the expected value of :math:`f`, i.e. :math:`f_(0,...,0)^2`
        where :math:`f_(0,...,0)` is a PCE coefficient of :math:`f`.
        """
        idx = self._mdx.mdx2idx[(0,)*self._mdx.dimension]
        return self._coeff[idx]

    def _computeVar(self):
        """ Compute PC expansion total variance.

        Compute the variance of :math:`f`, i.e.

        .. math::
            \\operatorname{Var} = \\sum_{\\alpha} f_\\alpha^2  - f_(0,...,0)^2,

        where :math:`f_\\alpha` are the PC expansion coefficients of :math:`f`.
        """
        _dim = self._mdx.dimension
        if (self._mdx.count == 1 and
                self._mdx.mdx[0] == np.zeros(_dim).reshape(1, -1)):
            return np.zeros(self._fEval.shape[1])
        else:
            return np.sum(self._coeff**2, axis=0) - self._mean**2

    def _computeSobolCoeff(self):
        """ Compute the Sobol coefficients.

        The Sobol coefficients are given as

        .. math::
            S_{i_1,...,i_k} = \\sum_{\\alpha\\in\mathcal{M}} f_\\alpha(x)^2

        where :math:`\\mathcal{M} = { \\alpha | \\alpha_{i_j} != 0 for j = 1,...,k }`.
        """
        sobolCoeff = np.zeros([len(self._mdx.sdx), self._fDim])
        # Get indices for non-zero entries of variance.
        nz_idx = np.nonzero(self._var)
        for jj, sdx in enumerate(self._mdx.sdx):
            mdx = self._mdx.sdx2mdx[sdx]
            idx = [self._mdx.mdx2idx[tuple(alpha)] for alpha in mdx]
            coeff = self._coeff[idx]
            sobolCoeff[jj, nz_idx] = (
                np.sum(coeff[:, nz_idx]**2, axis=0) / self._var[nz_idx]
            )
        return sobolCoeff

    def _assembleMatrices(self, basis):
        """ Assemble information and basis evaluation matrix.

        Assemble the information matrix :math:`A` and the basis evaluation
        matrix :math:`\\Psi` with the regression points of the PC expansion.
        The basis evaluation matrix :math:`\\Psi` is given by

        .. math::
            \\Psi_{kj} = \\operatorname{basis}[j](\\operatorname{regPoints}[k]).
        """
        if self._verbose:
            print('{}: Assemble information matrix ...'.format(pt.misc.now()))

        samples = self._regPoints[:self._regLength]
        W = self._weights[:self._regLength]

        # Evaluate basis functions.
        if self._basisMat is None:
            basisEvalMatrix = np.array([
                self._basis[jj](samples) for jj in range(self._mdx.count)
            ])
        else:
            basisEvalMatrix = self._basisMat.T

        # Assemble information matrix (Gramian matrix).
        if self._infoMatrix is None:
            # NOTE: Information matrix might require a lot of memory during
            # allocation. This code assures not total free memory is used.
            infoMatrix = np.zeros([self._mdx.count, self._mdx.count])
            batch_size = get_infoMat_batchsize(self._mdx.count)
            for batch in pt.misc.batch(range(samples.shape[0]), batch_size):
                infoMatrix += np.sum(
                    W[batch]
                    * basisEvalMatrix[:, batch].reshape(
                        1, basisEvalMatrix.shape[0], -1)
                    * basisEvalMatrix[:, batch].reshape(
                        basisEvalMatrix.shape[0], 1, -1),
                    axis=-1
                )
        else:
            infoMatrix = self._infoMatrix

        return infoMatrix, basisEvalMatrix.T, W

    def _checkParamAttributes(self, distDict):
        """ Check parameter validity.

        Check parameters for attributes needed to compute the polynomial chaos
        expansion.
        """
        for param in self._params:
            if param.distribution in distDict['uniform']:
                pass
            elif param.distribution in distDict['normal']:
                # Check if param.mean exists for normal distributions.
                if not hasattr(param, 'mean'):
                    text = 'Missing attribute for Parameter "' + param.name
                    text += '": mean'
                    raise AttributeError(text)
                # Check if param.variance exists for normal distributions.
                if not hasattr(param, 'variance'):
                    text = 'Missing attribute for Parameter "' + param.name
                    text += '": variance'
                    raise AttributeError(text)
            elif param.distribution in distDict['gamma']:
                # Check if param.alpha exists for beta distributions.
                if not hasattr(param, 'alpha'):
                    text = 'Missing attribute for Parameter "' + param.name
                    text += '": alpha'
                    raise AttributeError(text)
                # Check if param.beta exists for beta distributions.
                if not hasattr(param, 'beta'):
                    text = 'Missing attribute for Parameter "' + param.name
                    text += '": beta'
                    raise AttributeError(text)
            elif param.distribution in distDict['beta']:
                # Check if param.alpha exists for beta distributions.
                if not hasattr(param, 'alpha'):
                    text = 'Missing attribute for Parameter "' + param.name
                    text += '": alpha'
                    raise AttributeError(text)
                # Check if param.beta exists for beta distributions.
                if not hasattr(param, 'beta'):
                    text = 'Missing attribute for Parameter "' + param.name
                    text += '": beta'
                    raise AttributeError(text)
            else:
                raise ValueError(
                    'unknown distribution: {}'.format(param.distribution)
                )

    def approximation(self, x, partial=None):
        """ Evaluate the (partial derivative of the) PC approximation.

        Parameters
        ----------
        x : array_like
            Parameter realizations in which the approximation is evaluated.
        partial : list of int
            List that specifies the number of derivatives in each component.
            Length is the number of parameters.

        Returns
        -------
        array_like
            Evaluation of PC expansion in parameter realizations.
        """
        if not (0 < x.ndim < 3):
            raise ValueError('Wrong ndim: {}'.format(x.ndim))
        if x.ndim == 1:
            x.shape = 1, -1
        c = self._coeff.reshape(self._coeff.shape[0], 1, -1)
        m_basis = pt.basis.multivariate_basis(
            self._paramBasis, self._mdx.mdx, partial)
        b = np.array([m_basis[jj](x) for jj in range(self._mdx.count)])
        b.shape = b.shape[0], b.shape[1], 1
        return np.sum(c*b, axis=0)


class PolynomialChaosFrame(object):
    """ Computation of sparse PC expansion for each spatial component.

    .. deprecated:: 2.0.0
        `PolynomialChaosFrame` will be removed in PyThia 3.0.0, it is replaced
        by `PolynomialChaos` because the latter performs more efficiently.

    Compute the PC expansion of a function for given parameters for specified
    multiindices with linear regression. The coefficients are computed for
    each spatial component individually.

    Parameters
    ----------
    params : dict/list of `pythia.parameter.RandomParameter`
        Parameter to specify random variables for chaos expansion.
    mdx : `pythia.index.PCMultiIndex`
        Multiindices of coefficients of the polynomial chaos expansion.
    regPoints : array_like
        Regression points for linar regression (Parameter realizations).
    weights : array_like
        Regression weights for `regPoints`.
    fEval : array_like
        Function evaluation of `regPoints` and `xVal`.
    xVal : array_like, optional
        Spacial/physical point of function evaluation.

    Other Parameters
    ----------------
    infoMatrix : array_like, optional
        Information matrix (Gramian) of the basis functions and samples.
    basisMat : array_like, optional
        Basis evaluation matrix of samples.
    coeff : array_like, optional
        PC coefficients.
    regLength : int, default=0
        Number of regression points used in linear regression.
        Needs to be less or equal to length of mdx.
        Zero results in automatic choice of amount of sample points.
    verbose : bool, default=False
        Makes PCE talk.
    """
    # TODO(Nando): Properties should be easy to compute functions.
    #              For attributes, simply name those without leading '_'

    def __init__(self, params, mdx, regPoints, weights, fEval,
                 xVal, infoMatrix=None, basisMat=None, coeff=None, regLength=0,
                 verbose=False):
        """ Initiate the computation of the PC expansion of a function. """
        self._params = params
        if isinstance(self._params, dict):
            self._params = pt.misc.paramDictToList(params)
        assert isinstance(self._params, list)
        for param in self._params:
            assert isinstance(param, pt.parameter.RandomParameter)
        self._pDim = len(params)
        self._mdx = mdx
        assert isinstance(self._mdx, pt.index.PCMultiIndex)
        self._regPoints = regPoints
        assert self._regPoints.ndim == 2
        assert self._regPoints.shape[1] == len(self._params)
        self._weights = weights
        assert self._weights.ndim == 1
        assert self._weights.shape[0] == self._regPoints.shape[0]
        self._fEval = fEval
        assert self._fEval.ndim == 3
        assert self._fEval.shape[1] == self._regPoints.shape[0]
        self._fDim = self._fEval.shape[2]
        self._xVal = xVal
        if self._xVal is not None:
            assert self._xVal.ndim == 2
        self._xDim = self._xVal.shape[1]

        self._regLength = int(regLength)
        assert 0 <= self._regLength <= self._regPoints.shape[0]
        # Compute regression points for evalutation of PCE coefficients.
        if self._regLength == 0:
            self._regLength = pt.misc.wlsSamplingBound(self._mdx.count, c=2)

        self._infoMatrix = infoMatrix
        if self._infoMatrix is not None:
            assert self._infoMatrix.shape == (self._mdx.count, self._mdx.count)
        self._basisMat = basisMat
        if self._basisMat is not None:
            assert self._basisMat.shape == (self._regLength, self._mdx.count)
        self._coeff = coeff
        if self._coeff is not None:
            assert self._coeff.shape == (
                self._xVal.shape[0], self._mdx.count, self._fDim
            )

        self._verbose = verbose
        assert isinstance(self._verbose, bool)

        self._pce = PolynomialChaos(
            self._params, self._mdx, self._regPoints, self._weights,
            self._fEval[0], xVal=self._xVal[0], infoMatrix=self._infoMatrix,
            basisMat=self._basisMat, coeff=self._coeff,
            regLength=self._regLength
        )
        if self._infoMatrix is None:
            self._infoMatrix = self._pce.infoMatrix
        if self._basisMat is None:
            self._basisMat = self._pce.basisMat
        self._paramPDF = self._pce.paramPDF
        self._pdf = self._pce.pdf
        self._paramBasis = self._pce.paramBasis
        self._basis = self._pce.basis

        self._mean, self._var, self._sCoeff = None, None, None

    @property
    def parameter(self):
        """ List of parameters. """
        return self._params

    @property
    def mdx(self):
        """ Multiindices object. """
        return self._mdx

    @property
    def regPoints(self):
        """ Parameter realization used for training. """
        return self._regPoints

    @property
    def weights(self):
        """ Regression weights. """
        return self._weights

    @property
    def fEval(self):
        """ Function evaluations used for training. """
        return self._fEval

    @property
    def xVal(self):
        """ Spatial component. """
        return self._xVal

    @property
    def regLength(self):
        """ Number of used training data to compute PC expansion. """
        return self._regLength

    @property
    def pDim(self):
        """ Number of random parameters. """
        return self._pDim

    @property
    def xDim(self):
        """ Spatial dimension. """
        return self._xDim

    @property
    def fDim(self):
        """ Image dimension of the function. """
        return self._fDim

    @property
    def paramPDF(self):
        """ List of univariate PDFs for each parameter. """
        return self._paramPDF

    @property
    def pdf(self):
        """ Multivariate PDF of parameters. """
        return self._pdf

    @property
    def paramBasis(self):
        """ List of univariate basis functions for each parameter. """
        return self._paramBasis

    @property
    def basis(self):
        """ Multivariate basis functions used for the PC expansion. """
        return self._basis

    @property
    def infoMatrix(self):
        """ Information matrix (unscaled Gramian) for the samples. """
        return self._infoMatrix

    @property
    def basisMat(self):
        """ Basis evaluation matrix :math:`P_j(y_i)`. """
        return self._basisMat

    @property
    def coeff(self):
        """ Coefficients of the PC expansion. """
        return self._coeff

    @property
    def mean(self):
        """ Mean of the PC expansion. """
        return self._mean

    @property
    def variance(self):
        """ Variance of the PC expansion. """
        return self._var

    @property
    def std(self):
        """ Standard deviation of the PC expansion. """
        return np.sqrt(self._var)

    @property
    def sobolCoeff(self):
        """ Approximated Sobol indices for the PC expansion. """
        return self._sCoeff

    def run(self, coeff=None):
        """ Compute PC expansion for each spatial component individually.

        Compute the PC expansion coefficients for each spatial component
        without repeatedly assembling the information matrix.

        Parameters
        ----------
        coeff : array_like, optional
            Precomputed PC coefficients.

        Notes
        -----
        This method needs to be called separately after initiating a
        `PolynomialChaosFrame` object.
        """
        self._sCoeff = np.zeros(
            [self._xVal.shape[0], *self._pce.sobolCoeff.shape])
        self._mean = np.zeros([self._xVal.shape[0], self._fDim])
        self._var = np.zeros([self._xVal.shape[0], self._fDim])
        if self._coeff is None:
            self._coeff = np.zeros(
                [self._xVal.shape[0], *self._pce.coeff.shape])

        for jj, xVal in enumerate(self._xVal):
            if coeff is None:
                pc = PolynomialChaos(self._params, self._mdx, self._regPoints,
                                     self._weights, self._fEval[jj], xVal=xVal,
                                     infoMatrix=self._infoMatrix,
                                     basisMat=self._basisMat,
                                     paramPDF=self._paramPDF, pdf=self._pdf,
                                     paramBasis=self._paramBasis,
                                     basis=self._basis,
                                     regLength=self._regLength
                                     )
                self._coeff[jj] = pc.coeff
            else:
                pc = PolynomialChaos(self._params, self._mdx, self._regPoints,
                                     self._weights, self._fEval[jj], xVal=xVal,
                                     infoMatrix=self._infoMatrix,
                                     basisMat=self._basisMat,
                                     paramPDF=self._paramPDF, pdf=self._pdf,
                                     paramBasis=self._paramBasis,
                                     basis=self._basis,
                                     coeff=coeff[jj], regLength=self._regLength
                                     )
            self._mean[jj] = pc.mean
            self._var[jj] = pc.variance
            self._sCoeff[jj] = pc.sobolCoeff

    def approximation(self, x, partial=None):
        """ Evaluate the (partial derivative of the) PC approximation.

        Parameters
        ----------
        x : array_like
            Parameter realizations in which the approximation is evaluated.
        partial : list of int
            List that specifies the number of derivatives in each component.
            Length is the number of parameters.

        Returns
        -------
        array_like
            Evaluation of PC expansion in parameter realizations.
        """
        if not 0 < x.ndim < 3:
            raise ValueError('Wrong ndim: {}'.format(x.ndim))
        if x.ndim == 1:
            x.shape = 1, -1
        m_basis = pt.basis.multivariate_basis(
            self._paramBasis, self._mdx.mdx, partial)
        b = np.array([m_basis[jj](x) for jj in range(self._mdx.count)])
        c = self._coeff.reshape(
            self._coeff.shape[0], self._coeff.shape[1], 1, -1)
        b.shape = 1, b.shape[0], b.shape[1], 1
        return np.sum(c*b, axis=1)


def find_optimal_mdx(params, regPoints, weights, fEval, max_terms=0,
                     threshold=1e-03, get_sobol_coeff=False):
    """ Compute optimal multiindices of PCE.

    Compute the optimal multiindices for a polynomial chaos expansion based on
    an estimate of the Sobol coefficient values.

    Parameters
    ----------
    params : list of pythia.Parameters.RandomParameter
        Random parameters of the problem.
    regPoints : array_like
        Sample points for training
    weights : array_like
        Weights for training.
    fEval : array_like
        Function evaluations for training.
    max_terms : int, default=0
        Maximum number of expansion terms. Number of expansion terms is chosen
        automatically for `max_terms=0`.
    get_sobol_coeff : bool
        If true, function also return crude intermediate approximation of Sobol
        coefficient values.

    Returns
    -------
    mdx : pythia.Indices.PCMultiIndex
        Adaptive multiindices.
    sobolCoeff : array_like, optional
        Crude intermediate approximation of Sobol indices.
    """
    assert 0 <= threshold < 1
    # set maximal number of expansion terms
    regLength, nParams = regPoints.shape
    if max_terms > 0:
        _max_terms = max_terms
    else:
        _max_terms = int(regLength/np.log(regLength)/2)
    if _max_terms > int(regLength/np.log(regLength)/2):
        print("Warning. Gramian may become ill conditioned.")

    # compute crude approximation of Sobol coefficients
    sobolCoeff, sdx = get_sobol_coefficients(
        params, regPoints, weights, fEval, max_terms)

    # sort Sobol coefficients by largest and mark top threshold percent.
    idx, vals, marker = pt.misc.doerfler_marking(
        np.sum(sobolCoeff, axis=1), threshold=1-threshold)

    # assemble adaptive choice of multiindices
    mdx = assemble_mdx(idx[:marker], vals[:marker], sdx, nParams, _max_terms)

    if get_sobol_coeff:
        return mdx, sobolCoeff
    else:
        return mdx


def get_sobol_coefficients(params, regPoints, weights, fEval, max_terms):
    """ Compute rough estimate of Sobol coefficient.

    Compute an approximation of the Sobol coefficients with as many PC
    expansion terms as possible.

    Parameters
    ----------
    params: list of `pythia.parameter.RandomParameter`
        List of stochastic parameters.
    regPoints: array_like
        Parameter realizations.
    weights: array_like
        Regressio weights.
    fEval: array_like
        Function evaluations in regression points.
    max_terms: int
        Number of considered expansion terms.

    Returns
    -------
    pc.sobolCoeff : array_like
        Sobol indices.
    mdx.sdx : list of tuple
        Sobol index identifiers (subscripts).
    """
    regLength, nParams = regPoints.shape
    _max_terms = np.max([int(regLength/np.log(regLength)), max_terms])

    # get max polynimial degree for number of terms
    def fac(n):
        return float(np.math.factorial(n))
    for poly_deg in range(1000):
        n_terms = fac(poly_deg+nParams) / fac(poly_deg) / fac(nParams)
        if n_terms > _max_terms:
            break
        DEG = poly_deg

    mdx = pt.index.PCMultiIndex(nParams)
    mdx.mdx = mdx.mdxFromShape([DEG]*nParams)
    mdx.mdxLimitAbs(DEG)
    mdx.refresh()
    pc = PolynomialChaos(params, mdx, regPoints, weights, fEval)
    return pc.sobolCoeff, mdx.sdx


def assemble_mdx(IDXs, VALs, SDXs, nParams, max_terms):
    """ Compute automatic choice of multiindices.

    Parameters
    ----------
    IDXs : list
        Enumeration of all possible Sobol indices.
    VALs : array_like
        Values of Sobol indices.
    SDXs : list
        Sobol indices (subscripts, not the values).
    nParams : int
        Number of stochastic parameters.
    max_terms : int
        Maximum number of expansion terms.

    Returns
    -------
    mdx : `pythia.index.PCMultiIndex`
        Sparse multiindices.
    """
    mdx = pt.index.PCMultiIndex(nParams)
    mdx.mdx = np.zeros([1, nParams])  # include 0 mdx
    n_terms = max_terms-1
    n_terms_per_idx = np.array([int(n_terms/len(IDXs)) for val in VALs])
    mdx_list = [0]*len(IDXs)
    for i, idx in enumerate(IDXs):
        sdx = [v-1 for v in SDXs[idx]]  # current sdx
        deg = int(n_terms_per_idx[i]**(1/len(sdx))+1)
        mdx_list[i] = mdx.mdxAdd(
            sdx, [range(1, deg+2)]*len(sdx)
        )[1:n_terms_per_idx[i]+1]
    mdx_array = np.concatenate([mdx.mdx]+mdx_list, axis=0)
    mdx.mdx = np.array(mdx.mdxSort(mdx_array)[0], dtype=int)
    mdx.refresh()
    return mdx


def get_infoMat_batchsize(dim, save_memory=1025**3/2):
    """ Compute memory allocation batch sizes for information matrix.

    Compute the maximal number of samples in each batch when assembling the
    information matrix to be maximally memory efficient and avoid OutOfMemory
    errors.

    Parameters
    ----------
    dim : int
        Number of rows/columns of information matrix.
    save_memory : int, default=3*1025/2
        Memory (in bytes), that should be kept free. The default is equivalent
        to 512 MB.

    Returns
    -------
    n : int
        Batchsize for assembling of information matrix.
    """
    available_memory = psutil.virtual_memory().available
    mem = available_memory - save_memory
    n = int(mem / 8 / dim**2)
    if n < 1:
        # There is less memory available than required for at least one sample.
        raise MemoryError('Not enough free memory.')
    else:
        return n


if __name__ == '__main__':
    pass
