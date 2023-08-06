""" Provide Gaussian likelihoods for PC surrogates. """
import numpy as np
import warnings


class Gaussian(object):
    """ Gaussian likelihood function for differentiable forward problem.

    Assemble the Gaussian likelihood

    .. math::
        \\mathcal{L}(x) = \\frac{1}{(2\\pi)^{M/2}\\sqrt{\\det \\Sigma}} \\exp\\Bigl( -\\frac{1}{2} \\Vert \\Sigma^{-1/2}(f(x)-\\delta) \\Vert \\Bigr)

    for covariance matrix
    :math:`\\Sigma = \\operatorname{diag}(\\sigma_1(y_1),\\dots,\\sigma_M(y_M))`
    and measurement/observation :math:`\\delta`.

    Parameters
    ----------
    f : function
        Forward model.
    sigma : function
        Error model for standard deviation describing :math:`\\Sigma`.
    xdim : int
        Number of stochastic parameters.
    """

    def __init__(self, f, sigma, xdim):
        """ Initialize Gaussian likelihood object. """
        self._f = f
        self._std = sigma
        self._xdim = xdim

    def likelihood(self, x, y_meas):
        """ Evaluate the Gaussian likelihood with specified measurement.

        Parameters
        ----------
        x : array_like
            Realizations of stochastic parameters.
        y_meas : array_like
            Measurement :math:`\delta`.
        """
        # check dimensionality and reshape if necessary.
        y, f_val, std, mdim, fdim = self._reshape(x, y_meas)

        a = (2*np.pi)**(-mdim*fdim/2)  # float
        b = 1/np.prod(std, axis=(0, 2))**mdim  # shape: (#points,)
        c = np.prod(np.exp(-(f_val-y)**2/(2*std**2)),
                    axis=(0, 2))  # (#points,)

        return a*b*c

    def log_likelihood(self, x, y_meas):
        """ Evaluate the Gaussian log-likelihood with specified measurement.

        Parameters
        ----------
        x : array_like
            Realizations of stochastic parameters.
        y_meas : array_like
            Measurement :math:`\delta`.
        """
        # check dimensionality and reshape if necessary.
        y, f_val, std, mdim, fdim = self._reshape(x, y_meas)

        a = -mdim*fdim/2 * np.log(2*np.pi)  # float
        b = -mdim * np.sum(np.log(std), axis=(0, 2))  # (#points,)
        c = np.sum(-(f_val-y)**2/(2*std**2), axis=(0, 2))  # (#points,)

        return a+b+c

    def _reshape(self, x, y_meas):
        """ Check shape compatibility of input and reshape if necessary.

        Parameters
        ----------
        x : array_like
            Realizations of stochastic parameters.
        y_meas : array_like
            Measurement :math:`\delta`.
        """
        x_val = np.array(x)
        y_val = np.array(y_meas)
        # x shape: (#points, xdim)
        if x_val.ndim < 2:
            x_val.shape = 1, -1
        assert x_val.shape[1] == self._xdim
        # y_meas shape: (mdim, fdim)
        if y_val.ndim < 2:
            y_val.shape = 1, -1
        assert x_val.ndim == 2 and y_val.ndim == 2

        # get number of measurements and image dim of f
        mdim, fdim = y_val.shape

        f_val = self._f(x_val)
        # f_val shape: (#points, fdim)
        if f_val.ndim < 2:
            f_val.shape = 1, -1
        assert f_val.shape[1] == fdim

        std = self._std(x_val)
        # std shape: (#points, fdim)
        if std.ndim < 2:
            std.shape = 1, -1
        if std.shape[1] == 1:
            std = std*np.ones(fdim)
        assert std.shape[1] == fdim
        assert np.min(std) >= 0

        # Reshape for fast multiplication
        y = np.expand_dims(y_meas, axis=1)  # (mdim, 1, fdim)
        std = np.expand_dims(self._std(x_val), axis=0)  # (1, #points, fdim)
        f_val = np.expand_dims(f_val, axis=0)  # (1, #points, fdim)

        return y, f_val, std, mdim, fdim


def gauss_likelihood(p, y, error_model):
    """ Compute a gaussian likelihood function.

    .. deprecated:: 2.0.0
        `gauss_likelihood` will be removed in PyThia 3.0.0, it is replaced by
        the `Gaussian` class as the latter is clearer and more comfortable to
        use.

    Parameters
    ----------
    p : array_like
        Parameter realizations.
    y : array_like
        Measurement data :math:`\\delta`.
    error_model : function
        Function that maps `p` to two arrays containing the evaluation of the
        forward model `f(p)` and the standard deviation `\\sigma(p)`.
    """
    warnings.warn("Depreciated legacy code. Use Gaussian() instead.")
    if p.ndim < 2:
        p.shape = 1, -1
    if y.ndim < 2:
        y.shape = 1, -1
    assert p.ndim == 2 and y.ndim == 2

    f, std = error_model(p)  # shape is p.shape[0], y.shape[1] for each

    # Reshape for fast multiplication
    y = np.expand_dims(y, axis=1)
    std = np.expand_dims(std, axis=0)
    f = np.expand_dims(f, axis=0)

    val = np.exp(-(f-y)**2/(2*std**2)) / np.sqrt(2*np.pi) / std
    return np.prod(val, axis=(0, 2))
