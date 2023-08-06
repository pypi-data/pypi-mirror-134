""" Sampler classes for generating in random samples and PDF evaluations. """
import numpy as np
import scipy.stats
import time
import abc
import warnings
import pythia as pt


class Sampler(object):
    """ Base class for all continuous samplers. """
    __metaclass__ = abc.ABCMeta

    @property
    def dimension(self):
        """ Dimension of the ambient space. """
        return len(self.domain)

    @abc.abstractproperty
    def domain(self):
        """ Supported domain in ambient space.

        The domain of a sampler is a list of pairs representing the n-orthotope
        (hyperrectangle) where it is defined.
        """
        pass

    @abc.abstractmethod
    def pdf(self, point):
        """ Density of the samplers distribution.

        Computes the density of the samplers underlying distribution at the
        given `point`.

        Parameters
        ----------
        point : array_like of shape (..., D)
            List of points or single point. `D` is the objects dimension.

        Returns
        -------
        out : ndarray of shape (..., 1)
            Density at the point.
        """
        pass

    @abc.abstractmethod
    def sample(self, *shape):
        """ Random values in a given shape.

        Create an array of the given shape and populate it with random samples
        from the samplers distribution.

        Parameters
        ----------
        shape : array_like, optional
            The dimensions of the returned array, should all be positive.
            If no argument is given a single Python float is returned.

        Returns
        -------
        out : array_like
            Random values of specified shape.
        """
        pass

    @abc.abstractproperty
    def mass(self):
        """ Mass of the sampler distribution.

        The integral of the sampler distribution over the domain of
        definition. If the density is normalised this value should be one.
        """
        pass

    @classmethod
    def __subclasshook__(cls, C):
        def has(s):
            return any(s in B.__dict__ for B in C.__mro__)
        return (has("domain") and has("pdf") and has("sample") and
                has("dimension") and has("mass"))


class UniformSampler(Sampler):
    """ Sampler for univariate uniformly distributed samples on given domain.

    Parameters
    ----------
    domain : array_like
        Interval of support of distribution.
    """

    def __init__(self, domain):
        """ Initiate UniformSampler object. """
        self._domain = np.reshape(domain, (-1, 2))
        assert self._domain.shape == (1, 2)
        self._length = self._domain[0, 1] - self._domain[0, 0]

    @property
    def domain(self):
        """ Parameter domain of support. """
        return np.array(self._domain)

    @property
    def dimension(self):
        """ Dimension of the parameters. """
        return 1  # sampler for 1D

    @property
    def mass(self):
        """ Mass of the PDF. """
        return 1  # always normed

    @property
    def maximum(self):
        """ Maximum value of the PDF. """
        return 1 / self._length

    def pdf(self, x):
        """ Evaluate PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        return scipy.stats.uniform.pdf(
            x, loc=self._domain[0, 0], scale=self._length)

    def log_pdf(self, x):
        """ Evaluate log-PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of log-PDF evaluated in `x`.
        """
        return scipy.stats.uniform.logpdf(
            x, loc=self._domain[0, 0], scale=self._length)

    def grad_x_log_pdf(self, x):
        """ Evaluate gradient of log-PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of gradient (vector valued) of log-PDF evaluated in `x`.
        """
        return np.zeros_like(x)

    def hess_x_log_pdf(self, x):
        """ Evaluate Hessian of log-PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of Hessian (matrix valued) of log-PDF evaluated in `x`.
        """
        return np.zeros_like(x)

    def sample(self, *shape):
        """ Draw samples from distribution.

        Parameters
        ----------
        shape : array_like
            Shape of the samples.

        Returns
        -------
        array_like
            Random samples of specified shape.
        """
        return np.random.uniform(self._domain[0, 0], self._domain[0, 1], shape)

    def density(self, x):
        """ Evaluate PDF.

        .. deprecated:: 2.0.0
            `density` will be removed in PyThia 3.0.0, use `pdf` instead.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        warnings.warn("Function 'density' is deprecated. Use 'pdf' instead.")
        return self.pdf(x)


class NormalSampler(Sampler):
    """ Sampler for univariate normally distributed samples.

    Parameters
    ----------
    mean : float
        Mean of the Gaussian distribution.
    var : float
        Variance of the Gaussian distribution.
    """

    def __init__(self, mean, var):
        """ Initiate NormalSampler object. """
        self._domain = np.array([-np.inf, np.inf], ndmin=2)  # shape is (1,2)
        self._mean = mean
        assert var >= 0  # variance must be positive
        self._var = var

    @property
    def domain(self):
        """ Parameter domain of support. """
        return np.array(self._domain)

    @property
    def mass(self):
        """ Mass of the PDF. """
        return 1  # always normed

    @property
    def dimension(self):
        """ Dimension of the parameters. """
        return 1  # sampler for 1D

    @property
    def mean(self):
        """ Mean of the distribution. """
        return self._mean

    @property
    def var(self):
        """ Variance of the distribution. """
        return self._var

    @property
    def maximum(self):
        """ Maximum value of the PDF. """
        return self.pdf(self.mean)

    def pdf(self, x):
        """ Evaluate PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        return scipy.stats.norm.pdf(
            x, loc=self._mean, scale=np.sqrt(self._var))

    def log_pdf(self, x):
        """ Evaluate log-PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of log-PDF evaluated in `x`.
        """
        return scipy.stats.norm.logpdf(
            x, loc=self._mean, scale=np.sqrt(self._var))

    def grad_x_log_pdf(self, x):
        """ Evaluate gradient of log-PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of gradient (vector valued) of log-PDF evaluated in `x`.
        """
        return - (x - self._mean) / self._var

    def hess_x_log_pdf(self, x):
        """ Evaluate Hessian of log-PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of Hessian (matrix valued) of log-PDF evaluated in `x`.
        """
        return - 1 / self.var * np.ones_like(x)

    def sample(self, *shape):
        """ Draw samples from distribution.

        Parameters
        ----------
        shape : array_like
            Shape of the samples.

        Returns
        -------
        array_like
            Random samples of specified shape.
        """
        return np.random.normal(self._mean, np.sqrt(self._var), shape)

    def density(self, x):
        """ Evaluate PDF.

        .. deprecated:: 2.0.0
            `density` will be removed in PyThia 3.0.0, use `pdf` instead.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        warnings.warn("Function 'density' is deprecated. Use 'pdf' instead.")
        return self.pdf(x)


class GammaSampler(Sampler):
    """ Sampler for univariate Gamma distributed samples on given domain.

    Parameters
    ----------
    domain : array_like
        Supported domain of distribution.
    alpha : float
        Parameter for Gamma distribution.
    beta : float
        Parameter for Gamma distribution.
    """

    def __init__(self, domain, alpha, beta):
        """ Initiate GammaSampler object. """
        self._domain = np.reshape(domain, (-1, 2))
        assert self._domain.shape == (1, 2)
        assert self._domain[0, 1] == np.inf
        self._alpha = alpha
        self._beta = beta
        assert self._alpha > 0 and self._beta > 0

    @property
    def domain(self):
        """ Parameter domain of support. """
        return np.array(self._domain)

    @property
    def mass(self):
        """ Mass of the PDF. """
        return 1  # always normed

    @property
    def maximum(self):
        """ Maximum value of the PDF. """
        if not hasattr(self, '_maximum'):
            mean = self.alpha / self.beta + self.domain[0, 0]
            domain = np.array([self.domain[0, 0], 2*mean], ndmin=2)
            self._maximum = get_maximum(self.pdf, domain)
        return self._maximum

    @property
    def dimension(self):
        """ Dimension of the parameters. """
        return 1  # this is a 1D sampler

    @property
    def alpha(self):
        """ Parameter :math:`\\alpha` of Gamma distribution. """
        return self._alpha

    @property
    def beta(self):
        """ Parameter :math:`\\beta` of Gamma distribution. """
        return self._beta

    def pdf(self, x):
        """ Evaluate PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        y = x - self._domain[0, 0]
        return scipy.stats.gamma.pdf(y, a=self._alpha, scale=1.0/self._beta)

    def log_pdf(self, x):
        """ Evaluate log-PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of log-PDF evaluated in `x`.
        """
        y = x - self._domain[0, 0]
        return scipy.stats.gamma.logpdf(y, a=self._alpha, scale=1.0/self._beta)

    def grad_x_log_pdf(self, x):
        """ Evaluate gradient of log-PDF.

        .. note::
            Not yet implemented.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of gradient (vector valued) of log-PDF evaluated in `x`.
        """
        raise NotImplementedError

    def hess_x_log_pdf(self, x):
        """ Evaluate Hessian of log-PDF.

        .. note::
            Not yet implemented.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of Hessian (matrix valued) of log-PDF evaluated in `x`.
        """
        raise NotImplementedError

    def sample(self, *shape):
        """ Draw samples from distribution.

        Parameters
        ----------
        shape : array_like
            Shape of the samples.

        Returns
        -------
        array_like
            Random samples of specified shape.
        """
        SAMPLE = np.random.gamma(self._alpha, 1.0/self._beta, shape)
        return SAMPLE + self._domain[0, 0]

    def density(self, x):
        """ Evaluate PDF.

        .. deprecated:: 2.0.0
            `density` will be removed in PyThia 3.0.0, use `pdf` instead.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        warnings.warn("Function 'density' is deprecated. Use 'pdf' instead.")
        return self.pdf(x)


class BetaSampler(Sampler):
    """ Sampler for univariate Beta distributed samples on given domain.

    Parameters
    ----------
    domain : array_like
        Supported domain of distribution.
    alpha : float
        Parameter for Beta distribution.
    beta : float
        Parameter for Beta distribution.
    """

    def __init__(self, domain, alpha, beta):
        """ Initiate BetaSampler object. """
        self._domain = np.reshape(domain, (-1, 2))
        assert self._domain.shape == (1, 2)
        self._length = self._domain[0, 1] - self._domain[0, 0]
        self._alpha = alpha
        self._beta = beta
        assert self._alpha > 0 and self._beta > 0

    @property
    def domain(self):
        """ Parameter domain of support. """
        return np.array(self._domain)

    @property
    def mass(self):
        """ Mass of the PDF. """
        return 1  # always normed

    @property
    def maximum(self):
        """ Maximum value of the PDF. """
        if not hasattr(self, '_maximum'):
            self._maximum = get_maximum(self.pdf, self.domain)
        return self._maximum

    @property
    def dimension(self):
        """ Dimension of the parameters. """
        return 1  # sampler for 1D

    @property
    def alpha(self):
        """ Parameter :math:`\\alpha` of Gamma distribution. """
        return self._alpha

    @property
    def beta(self):
        """ Parameter :math:`\\beta` of Gamma distribution. """
        return self._beta

    def pdf(self, x):
        """ Evaluate PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        y = pt.misc.shiftCoord(x, self._domain.flatten(), [0, 1])
        ret = scipy.stats.beta.pdf(y, a=self._alpha, b=self._beta)
        return ret / self._length

    def log_pdf(self, x):
        """ Evaluate log-PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of log-PDF evaluated in `x`.
        """
        y = pt.misc.shiftCoord(x, self._domain.flatten(), [0, 1])
        ret = scipy.stats.beta.logpdf(y, a=self._alpha, b=self._beta)
        return ret / self._length

    def grad_x_log_pdf(self, x):
        """ Evaluate gradient of log-PDF.

        .. note::
            Not yet implemented.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of gradient (vector valued) of log-PDF evaluated in `x`.
        """
        raise NotImplementedError

    def hess_x_log_pdf(self, x):
        """ Evaluate Hessian of log-PDF.

        .. note::
            Not yet implemented.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of Hessian (matrix valued) of log-PDF evaluated in `x`.
        """
        raise NotImplementedError

    def sample(self, *shape):
        """ Draw samples from distribution.

        Parameters
        ----------
        shape : array_like
            Shape of the samples.

        Returns
        -------
        array_like
            Random samples of specified shape.
        """
        SAMPLE = np.random.beta(self._alpha, self._beta, shape)
        return pt.misc.shiftCoord(SAMPLE, [0, 1], self._domain.flatten())

    def density(self, x):
        """ Evaluate PDF.

        .. deprecated:: 2.0.0
            `density` will be removed in PyThia 3.0.0, use `pdf` instead.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        warnings.warn("Function 'density' is deprecated. Use 'pdf' instead.")
        return self.pdf(x)


class RejectionSampler(Sampler):
    """ Rejection sampler for sampling arbitrary n-dimensional densities.

    Parameters
    ----------
    domain : array_like
        Domain of definition of density
    pdf : function
        Target density to generate samples from.
    trialSampler : `pythia.sampler.Sampler`
        Sampler for trial distribution, should generate samples fast.
    maximum : float, optional
        Threshold parameter with ``density <= maximum * sampler.pdf``
    """

    def __init__(self, domain, pdf, trialSampler, maximum=None):
        """ Initiate RejectionSampler object. """
        self._domain = np.reshape(domain, (-1, 2))
        self._pdf = pdf
        self._trialSampler = trialSampler
        assert isinstance(self._trialSampler, Sampler)
        self._maximum = maximum

    @property
    def domain(self):
        """ Parameter domain of support. """
        return np.array(self._domain)

    @property
    def mass(self):
        """ Mass of the PDF.

        .. note::
            The PDF is assumed to be normalized. This is not computed here.
        """
        return 1

    @property
    def maximum(self):
        """ Maximum value of the PDF. """
        if self._maximum is None:
            self._maximum = get_maximum(self.pdf, self.domain)
        return self._maximum

    @property
    def dimension(self):
        """ Dimension of the parameters. """
        return self._domain.shape[0]

    def pdf(self, x):
        """ Evaluate PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        return self._pdf(x)

    def sample(self, *shape):
        """ Draw samples from distribution.

        Parameters
        ----------
        shape : array_like
            Shape of the samples.

        Returns
        -------
        array_like
            Random samples of specified shape.
        """
        trial_samples = self._trialSampler.sample(np.prod(shape))
        SAMPLE = np.empty_like(trial_samples)
        pointer = 0
        while pointer < np.prod(shape):
            trial_samples = self._trialSampler.sample(np.prod(shape))
            checker = np.random.rand(trial_samples.shape[0])
            bulk = max(self.maximum, 1)
            isValidSample = (
                checker * bulk * self._trialSampler.pdf(trial_samples)
                <= self._pdf(trial_samples)
            )
            tmp = trial_samples[isValidSample]
            start = pointer
            end = min(pointer+tmp.shape[0], np.prod(shape))
            SAMPLE[start:end] = tmp[0:min(
                tmp.shape[0], np.prod(shape)-pointer)]
            pointer = end
        if self.dimension > 1:
            return np.moveaxis(SAMPLE.T.reshape(self.dimension, *shape), 0, -1)
        else:
            return SAMPLE.reshape(*shape)

    def density(self, x):
        """ Evaluate PDF.

        .. deprecated:: 2.0.0
            `density` will be removed in PyThia 3.0.0, use `pdf` instead.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        warnings.warn("Function 'density' is deprecated. Use 'pdf' instead.")
        return self.pdf(x)


class ProductSampler(Sampler):
    """ Tensor sampler for independent parameters.

    Sampler for cartesian product samples of a list of (independent) univariate
    samplers.

    Parameters
    ----------
    samplerList : list of `pythia.sampler.Sampler`
        List of (univariate) Sampler objects.
    """

    def __init__(self, samplerList):
        """ Initiate ProductSampler object. """
        self._samplers = list(samplerList)
        self._dim = len(self._samplers)
        self._domain = np.squeeze(np.array([s.domain for s in self._samplers]))
        # Add dimension if len(samplerList) == 1.
        if len(self._domain.shape) < 2:
            self._domain.shape = 1, 2
        assert self._domain.shape == (self._dim, 2)  # assert 1D samplers

    @property
    def domain(self):
        """ Parameter domain of support. """
        return np.array(self._domain)

    @property
    def mass(self):
        """ Mass of the PDF. """
        return np.prod(np.array([s.mass for s in self._samplers]))

    @property
    def maximum(self):
        """ Maximum value of the PDF. """
        if not hasattr(self, '_maximum'):
            self._maximum = get_maximum(self.pdf, self.domain)
        return self._maximum

    @property
    def dimension(self):
        """ Dimension of the parameters. """
        return self._dim

    def pdf(self, x):
        """ Evaluate PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        assert x.shape[-1] == self.dimension
        densities = [s.pdf for s in self._samplers]
        val = np.array(
            [densities[jj](x[..., jj]) for jj in range(self._dim)])
        return np.prod(val, axis=0)

    def log_pdf(self, x):
        """ Evaluate log-PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of log-PDF evaluated in `x`.
        """
        assert x.shape[-1] == self.dimension
        densities = [s.log_pdf for s in self._samplers]
        val = np.array(
            [densities[jj](x[..., jj]) for jj in range(self._dim)])
        return np.sum(val, axis=0)

    def grad_x_log_pdf(self, x):
        """ Evaluate gradient of log-PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of gradient (vector valued) of log-PDF evaluated in `x`.
        """
        grad_densities = [s.grad_x_log_pdf for s in self._samplers]
        return np.array(
            [grad_densities[jj](x[..., jj]) for jj in range(self._dim)]
            ).T

    def hess_x_log_pdf(self, x):
        """ Evaluate Hessian of log-PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of Hessian (matrix valued) of log-PDF evaluated in `x`.
        """
        # create an (x.shape[0], self._dim, self._dim) tensor where each
        # (self._dim, self._dim) matrix is the identity
        eye = np.tile(np.expand_dims(np.eye(self._dim), 0), (x.shape[0], 1, 1))

        # create an (x.shape[0],self._dim,1) tensor where each (x.shape[0],1,1)
        # subtensor is a diagonal entry of the hessian
        hess_densities = [s.hess_x_log_pdf for s in self._samplers]
        hess = np.expand_dims(np.array(
            [hess_densities[jj](x[..., jj]) for jj in range(self._dim)]
        ).T, 2)
        return eye*hess

    def sample(self, *shape):
        """ Draw samples from distribution.

        Parameters
        ----------
        shape : array_like
            Shape of the samples.

        Returns
        -------
        array_like
            Random samples of specified shape.
        """
        SAMPLE = [s.sample(*shape) for s in self._samplers]
        return np.stack(SAMPLE, -1)

    def density(self, x):
        """ Evaluate PDF.

        .. deprecated:: 2.0.0
            `density` will be removed in PyThia 3.0.0, use `pdf` instead.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        warnings.warn("Function 'density' is deprecated. Use 'pdf' instead.")
        return self.pdf(x)


class ConstraintSampler(Sampler):
    """ Sampler that applies algebraic constraints when sampling.

    Parameters
    ----------
    sampler : Sampler
        Sampler to sample from.
    constraints : list
        List of functions that return True if sample point satisfies the
        constraint.

    Notes
    -----
    The constaints may lead to a non-normalized density function.
    """

    def __init__(self, sampler, constraints):
        """ Initiate ConstraintSampler object. """
        self._sampler = sampler
        self._constraints = constraints
        assert hasattr(self._constraints, '__iter__')

    @property
    def constraints(self):
        """ Specified constrains. """
        return self._constraints

    @property
    def domain(self):
        """ Parameter domain of support. """
        return self._sampler.domain

    @property
    def mass(self):
        """ Mass of the PDF. """
        return self._sampler.mass

    @property
    def maximum(self):
        """ Maximum value of the PDF. """
        return self._sampler.maximum

    @property
    def dimension(self):
        """ Dimension of the parameters. """
        return self._sampler.dimension

    def pdf(self, x):
        """ Evaluate PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        return self._sampler.pdf(x)

    def sample(self, *shape):
        """ Draw samples from distribution.

        Parameters
        ----------
        shape : array_like
            Shape of the samples.

        Returns
        -------
        array_like
            Random samples of specified shape.
        """
        SAMPLE = self._sampler.sample(np.prod(shape))
        jTestSample = 0
        tic = time.time()
        for jj, sample in enumerate(SAMPLE):
            metConstraints = all([c(sample) for c in self._constraints])
            while not metConstraints:
                if jTestSample == 0:
                    testSample = self._sampler.sample(np.prod(shape))
                metConstraints = all(
                    [c(testSample[jTestSample]) for c in self._constraints]
                )
                if metConstraints:
                    SAMPLE[jj] = testSample[jTestSample]
                jTestSample = (jTestSample + 1) % np.prod(shape)
        return np.moveaxis(SAMPLE.T.reshape(self.dimension, *shape), 0, -1)

    def density(self, x):
        """ Evaluate PDF.

        .. deprecated:: 2.0.0
            `density` will be removed in PyThia 3.0.0, use `pdf` instead.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        warnings.warn("Function 'density' is deprecated. Use 'pdf' instead.")
        return self.pdf(x)


class ParameterSampler(Sampler):
    """ Product sampler of given parameters.

    Parameters
    ----------
    params : list of `pythia.parameter.RandomParameter`
        List or dictionary containing information of parameters.
    """

    def __init__(self, params):
        """ Initiate ParameterSampler object. """
        self._parameter = params
        if isinstance(self._parameter, dict):
            self._parameter = pt.misc.paramDictToList(params)
        assert isinstance(self._parameter, list)
        self._domain = np.array([param.domain for param in self._parameter])
        self._productSampler = ProductSampler(
            [assign_sampler(param) for param in self._parameter]
        )

    @property
    def parameter(self):
        """ List of parameters. """
        return self._parameter

    @property
    def domain(self):
        """ Parameter domain of support. """
        return self._domain

    @property
    def mass(self):
        """ Mass of the PDF.

        .. note::
            The PDF is assumed to be normalized. This is not computed here.
        """
        return 1

    @property
    def maximum(self):
        """ Maximum value of the PDF. """
        if not hasattr(self, '_maximum'):
            self._maximum = get_maximum(self.pdf, self.domain)
        return self._maximum

    @property
    def dimension(self):
        """ Dimension of the parameters. """
        return len(self._parameter)

    def weight(self, x):
        """ Weights for the parameter product PDF sampler. """
        return np.ones_like(self._productSampler.pdf(x))

    def pdf(self, x):
        """ Evaluate PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        return self._productSampler.pdf(x)

    def sample(self, *shape):
        """ Draw samples from distribution.

        Parameters
        ----------
        shape : array_like
            Shape of the samples.

        Returns
        -------
        array_like
            Random samples of specified shape.
        """
        return self._productSampler.sample(*shape)

    def density(self, x):
        """ Evaluate PDF.

        .. deprecated:: 2.0.0
            `density` will be removed in PyThia 3.0.0, use `pdf` instead.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        warnings.warn("Function 'density' is deprecated. Use 'pdf' instead.")
        return self.pdf(x)


class WLSSampler(Sampler):
    """ Weighted Least-Squares sampler as in Cohen & Migliorati 2017.

    Parameters
    ----------
    trialSampler : `pythia.sampler.Sampler`
        Trial sampler to draw samples from.
    basis : dict
        Dictionary of basis functions.
    strategy : string, ('rejection', 'sequential')
        Strategy for Sampling.

    Other Parameters
    ----------------
    paramBasis : dict of dict of function, optional
        Univariate basis functions for all parameter.
    alphas : list of tuple, optional
        List of Multiindices represented by tuples.
    tsa : bool, default=False
        Trial sampler adaptation. If True, a trial sampler is chosen on the
        distributions of parameters, if false a uniform trial sampler is used.
    """

    def __init__(self, params, basis, strategy='rejection',
                 paramBasis=None, alphas=None, tsa=True):
        """ Initiate WLSSampler object. """
        self._params = params
        if isinstance(self._params, dict):
            self._params = pt.misc.paramDictToList(params)
        assert isinstance(self._params, list)
        self._basis = basis
        self._strategy = strategy
        self._paramBasis = paramBasis
        self._alphas = alphas
        assert self._strategy in ('rejection', 'sequential')
        if self._strategy == 'rejection':
            self._wlsSampler = WLSRejectionSampler(
                self._params, self._basis, tsa=tsa)
        elif self._strategy == 'sequential':
            assert not self._paramBasis is None
            assert not self._alphas is None
            self._wlsSampler = WLSSequentialSampler(
                self._params, self._basis, self._paramBasis, self._alphas
            )

    @property
    def domain(self):
        """ Parameter domain of support. """
        return self._wlsSampler.domain

    @property
    def basis(self):
        """ Employed basis functions. """
        return self._basis

    @property
    def trialSampler(self):
        """ Trial sampler used for the rejection sampling. """
        return self._wlsSampler._trialSampler

    @property
    def mass(self):
        """ Mass of the PDF. """
        return 1

    @property
    def maximum(self):
        """ Maximum value of the PDF. """
        if not hasattr(self, '_maximum'):
            self._maximum = get_maximum(self.pdf, self.domain)
        return self._maximum

    @property
    def dimension(self):
        """ Dimension of the parameters. """
        return self._wlsSampler.dimension

    def weight(self, x):
        """ Weights for the PDF sampler. """
        return self._wlsSampler.weight(x)

    def pdf(self, x):
        """ Evaluate PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        return self._wlsSampler.pdf(x)

    def sample(self, *shape):
        """ Draw samples from distribution.

        Parameters
        ----------
        shape : array_like
            Shape of the samples.

        Returns
        -------
        array_like
            Random samples of specified shape.
        """
        return self._wlsSampler.sample(*shape)

    def density(self, x):
        """ Evaluate PDF.

        .. deprecated:: 2.0.0
            `density` will be removed in PyThia 3.0.0, use `pdf` instead.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        warnings.warn("Function 'density' is deprecated. Use 'pdf' instead.")
        return self.pdf(x)


class WLSTensorSampler(Sampler):
    """ WLS sampler for tensor multivariate basis.

    Sampler for weighted Least-Squares sampling as described by Cohen and
    Migliorati. Only full tensor space can be sampled. This allows for
    univariate weighted Least-Squares sampling in each component.

    Parameters
    ----------
    params : list of `pythia.parameter.RandomParameter`
        Parameter list.
    deg : int
        Polynomial degree of each component (same for all).
    tsa : bool, default=True
        Trial sampler adaptation. If True, a trial sampler is chosen on the
        distributions of parameters, if false a uniform trial sampler is
        used.
    """

    def __init__(self, params, deg, tsa=True):
        """ Initiate WLSTensorSampler object. """
        self._params = params
        if isinstance(self._params, dict):
            self._params = pt.misc.paramDictToList(params)
        assert isinstance(self._params, list)
        self._deg = deg
        self._uBasis = pt.basis.univariate_basis(params, self._deg)
        self._paramSampler = [assign_sampler(param) for param in self._params]

    @property
    def domain(self):
        """ Parameter domain of support. """
        return np.array([param.domain for param in self._params])

    @property
    def degree(self):
        """ Polynomial degree for each component. """
        return self._deg

    @property
    def mass(self):
        """ Mass of the PDF.

        .. note::
            The PDF is assumed to be normalized. This is not computed here.
        """
        return 1

    @property
    def maximum(self):
        """ Maximum value of the PDF. """
        if not hasattr(self, '_maximum'):
            self._maximum = get_maximum(self.pdf, self.domain)
        return self._maximum

    @property
    def dimension(self):
        """ Dimension of the parameters. """
        return len(self._params)

    def univariateWeight(self, x):
        """ Weights for the univariate components.

        Parameters
        ----------
        x : array_like
            Points the weight function is evaluated in.

        Returns
        -------
        w : array_like
            weights of evaluation points `x`.
        """
        w = np.zeros([len(self._params), x.shape[0]])
        for j in range(len(self._params)):
            b_eval = np.sum(np.array(
                [np.abs(b(x[:, j]))**2 for b in self._uBasis[j]]
            ), axis=0)
            w[j] = (self._deg[j] + 1) / b_eval
        return w

    def weight(self, x):
        """ Weights for the PDF.

        Parameters
        ----------
        x : array_like
            Points the weight function is evaluated in.

        Returns
        -------
        w : array_like
            weights of evaluation points `x`.
        """
        return np.prod(self.univariateWeight(x), axis=0)

    def univariateDensity(self, x):
        """ Evaluate univariate PDFs.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of univariate PDFs evaluated in `x`.
        """
        dens = np.zeros([len(self._params), x.shape[0]])
        for j, x_i in enumerate(x.T):
            dens[j] = self._paramSampler[j].pdf(x_i)
        return dens / self.univariateWeight(x)

    def pdf(self, x):
        """ Evaluate PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        return np.prod(self.univariateDensity(x), axis=0)

    def sample(self, *shape):
        """ Draw samples from distribution.

        Parameters
        ----------
        shape : array_like
            Shape of the samples.

        Returns
        -------
        array_like
            Random samples of specified shape.
        """
        samples = np.empty([*shape, len(self._params)])
        for j, param in enumerate(self._params):
            mBasis = pt.basis.multivariate_basis(
                [self._uBasis[j]],
                np.array(range(self._deg[j]+1)).reshape(-1, 1)
            )
            rSampler = WLSRejectionSampler([self._params[j]], mBasis, tsa=True)
            samples[:, j] = rSampler.sample(*shape)
        return samples

    def density(self, x):
        """ Evaluate PDF.

        .. deprecated:: 2.0.0
            `density` will be removed in PyThia 3.0.0, use `pdf` instead.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        warnings.warn("Function 'density' is deprecated. Use 'pdf' instead.")
        return self.pdf(x)


class WLSRejectionSampler(Sampler):
    """ WLS rejection sampler.

    Sampler for weighted Least-Squares sampling as described by Cohen and
    Migliorati. Uses rejection sampling for the weighted Least-Squares
    density.

    Parameters
    ----------
    params : list of `pythia.parameter.RandomParameter`
        List of parameters.
    basis : dict
        Dictionary of basis functions.
    tsa : bool
        Trial sampler adaptation. If True, a trial sampler is chosen on the
        distributions of parameters, if false a uniform trial sampler is
        used.
    """

    def __init__(self, params, basis, tsa):
        """ Initiate WLSRejectionSampler object. """
        self._params = params
        self._basis = basis
        self._paramSampler = ParameterSampler(params)
        self._trialSampler, self._bulk = self._tsa(tsa)

    @property
    def domain(self):
        """ Parameter domain of support. """
        return self._paramSampler.domain

    @property
    def basis(self):
        """ Employed basis functions. """
        return self._basis

    @property
    def trialSampler(self):
        """ Trial sampler used for the rejection sampling. """
        return self._trialSampler

    @property
    def mass(self):
        """ Mass of the PDF. """
        return 1

    @property
    def maximum(self):
        """ Maximum value of the PDF. """
        if not hasattr(self, '_maximum'):
            self._maximum = get_maximum(self.pdf, self.domain)
        return self._maximum

    @property
    def dimension(self):
        """ Dimension of the parameters. """
        return self._paramSampler.dimension

    def _tsa(self, tsa):
        """ Compute adapted trial sampler.

        Parameters
        ----------
        tsa : bool
            Adapt trial sampler or simply use uniform product sampler.

        Returns
        -------
        trialSampler : `pythia.sampler.Sampler`
            Trial sampler.
        bulk : array_like
            Domain estimate of the mass of the distribution.
        """
        s = ParameterSampler(self._params)
        sampler_list = []
        if tsa:
            for param in s.parameter:
                if param.distribution in 'uniform':
                    sampler_list.append(BetaSampler(param.domain, .5, .5))
                else:
                    sampler_list.append(UniformSampler(param.domain))
            trialSampler = ProductSampler(sampler_list)
        else:
            trialSampler = ProductSampler([
                UniformSampler(domain) for domain in s.domain
            ])
        bulk = get_maximum(
            lambda x: self.pdf(x)/trialSampler.pdf(x), self.domain
        )
        return trialSampler, bulk

    def weight(self, x):
        """ Weights for the PDF.

        Parameters
        ----------
        x : array_like
            Points the weight function is evaluated in.

        Returns
        -------
        w : array_like
            weights of evaluation points `x`.
        """
        m = len(self.basis)
        km = np.sum([abs(basis(x))**2 for basis in self.basis], axis=0)
        return m / km

    def pdf(self, x):
        """ Evaluate PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        if x.ndim == 1:
            x.shape = -1, 1
        assert x.shape[-1] == self.dimension
        return np.squeeze(self._paramSampler.pdf(x) / self.weight(x))

    def sample(self, *shape):
        """ Draw samples from distribution.

        Parameters
        ----------
        shape : array_like
            Shape of the samples.

        Returns
        -------
        array_like
            Random samples of specified shape.
        """
        sList = [UniformSampler(domain)
                 for domain in self._trialSampler.domain]
        pSampler = ProductSampler(sList)
        height = np.prod([sampler.maximum for sampler in sList])
        rsSampler = RejectionSampler(
            self.domain, self.pdf, self.trialSampler, self._bulk)
        return rsSampler.sample(*shape)

    def density(self, x):
        """ Evaluate PDF.

        .. deprecated:: 2.0.0
            `density` will be removed in PyThia 3.0.0, use `pdf` instead.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        warnings.warn("Function 'density' is deprecated. Use 'pdf' instead.")
        return self.pdf(x)


class WLSConditionalSampler(Sampler):
    """ WLS univariate conditional Sampler as described by Cohen & Migliorati.

    Parameters
    ----------
    params : dict
        Dictionary of pythia.Parameters.Parameter.
    basis : dict
        Dictionary of basis functions for all parameters in params.
    alphas : list
        List of tuples representing multiindices.
    condition : array_like
        Array of condition for sampling.

    .. note:: This is implemented very inefficiently.
    """

    def __init__(self, params, basis, alphas, condition=np.array([])):
        """ Initiate WLSConditionalSampler object. """
        self._basis = basis
        self._alphas = alphas

        paramSampler = ParameterSampler(params)
        self._parameter = paramSampler.parameter

        self._cond = condition
        assert len(self._cond.shape) == 1
        assert len(self._cond) < len(self._parameter)

        self._pos = self._cond.shape[0]
        assert 0 <= self._pos <= len(self._parameter)

        self._domain = paramSampler.domain[self._pos].reshape(-1, 2)
        self._basisDict = self._evalBasis()

        self._trialSampler = UniformSampler(self._parameter[self._pos].domain)

    @property
    def domain(self):
        """ Parameter domain of support. """
        return self._domain

    @property
    def dimension(self):
        """ Dimension of the parameters. """
        return 1

    @property
    def position(self):
        """ Parameter index. """
        return self._pos

    @property
    def mass(self):
        """ Mass of the PDF. """
        return 1

    @property
    def maximum(self):
        """ Maximum value of the PDF. """
        if not hasattr(self, '_maximum'):
            self._maximum = get_maximum(self.pdf, self.domain)
        return self._maximum

    @property
    def parameter(self):
        """ Parameter list. """
        return self._parameter

    @property
    def trialSampler(self):
        """ Trial sampler used for the rejection sampling. """
        return self._trialSampler

    def _evalBasis(self):
        """ Evaluate basis functions. """
        # TODO(Nando): Use cap var names only for constants.
        EVAL = {}
        self._deg = np.max(np.array(self._alphas), axis=0)
        for jj in range(self._pos):
            EVAL[jj] = {}
            for jDeg in range(self._deg[jj]+1):
                if len(self._cond) < 1:
                    EVAL[jj][jDeg] = 1.0
                else:
                    EVAL[jj][jDeg] = abs(
                        self._basis[jj][jDeg](self._cond[jj])
                    )**2
        return EVAL

    def pdf(self, x):
        """ Evaluate PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        # TODO(Nando): Use cap var names only for constants.
        numerator = [0]*len(self._alphas)
        denominator = [0]*len(self._alphas)
        for jAlpha, alpha in enumerate(self._alphas):
            prod = np.prod(
                [self._basisDict[jj][alpha[jj]] for jj in range(self._pos)],
                axis=0
            )
            basis = self._basis[self._pos][alpha[self._pos]](x)
            dens = assign_sampler(self._parameter[self._pos]).pdf(x)
            numerator[jAlpha] = (
                abs(basis)**2 * prod
            )
            denominator[jAlpha] = prod
        DENS = (
            dens
            * np.sum(numerator, axis=0)
            / np.sum(denominator, axis=0)
        )
        return DENS

    def sample(self, *shape):
        """ Draw samples from distribution.

        Parameters
        ----------
        shape : array_like
            Shape of the samples.

        Returns
        -------
        array_like
            Random samples of specified shape.
        """
        rsSampler = RejectionSampler(
            self.domain,
            self.pdf,
            self._trialSampler,
            max(1, self.maximum / self._trialSampler.maximum)
        )
        return rsSampler.sample(*shape)

    def density(self, x):
        """ Evaluate PDF.

        .. deprecated:: 2.0.0
            `density` will be removed in PyThia 3.0.0, use `pdf` instead.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        warnings.warn("Function 'density' is deprecated. Use 'pdf' instead.")
        return self.pdf(x)


class WLSSequentialSampler(Sampler):
    """ WLS sequential conditional sampler as in Cohen & Migliorati 2017.

    Parameters
    ----------
    params : dict of pythia.parameter.RandomParameter
    basis : dict of function
        Multivariate basis functions.
    paramBasis : dict of dict of function
        Univariate basis functions for all parameter.
    alphas : list of tuple
        List of Multiindices represented by tuples.
    """

    def __init__(self, params, basis, paramBasis, alphas):
        """ Initiate WLSSequentialSampler object. """
        self._params = params
        self._basis = basis
        self._paramBasis = paramBasis
        self._alphas = alphas
        self._paramSampler = ParameterSampler(params)

    @property
    def domain(self):
        """ Parameter domain of support. """
        return self._paramSampler.domain

    @property
    def dimension(self):
        """ Dimension of the parameters. """
        return self.domain.shape[0]

    @property
    def parameter(self):
        """ Parameter list. """
        return self._paramSampler.parameter

    @property
    def alphas(self):
        """ List of Multiindices represented by tuples. """
        return self._alphas

    @property
    def mass(self):
        """ Mass of the PDF. """
        return 1

    @property
    def maximum(self):
        """ Maximum value of the PDF. """
        if not hasattr(self, '_maximum'):
            self._maximum = get_maximum(self.pdf, self.domain)
        return self._maximum

    def weight(self, x):
        """ Weights for the PDF.

        Parameters
        ----------
        x : array_like
            Points the weight function is evaluated in.

        Returns
        -------
        w : array_like
            weights of evaluation points `x`.
        """
        return WLSRejectionSampler(self._params, self._basis).weight(x)

    def pdf(self, x):
        """ Evaluate PDF.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        return WLSRejectionSampler(self._params, self._basis).pdf(x)

    def sample(self, *shape):
        """ Draw samples from distribution.

        Parameters
        ----------
        shape : array_like
            Shape of the samples.

        Returns
        -------
        array_like
            Random samples of specified shape.
        """
        SAMPLE = np.empty([np.prod(shape), self.dimension])
        for jSample in range(np.prod(shape)):
            for jj in range(self.dimension):
                condSampler = WLSConditionalSampler(
                    self._params, self._paramBasis, self._alphas,
                    SAMPLE[jSample, 0:jj]
                )
                SAMPLE[jSample, jj] = condSampler.sample(1)
        return SAMPLE

    def density(self, x):
        """ Evaluate PDF.

        .. deprecated:: 2.0.0
            `density` will be removed in PyThia 3.0.0, use `pdf` instead.

        Parameters
        ----------
        x : array_like
            Evaluation points.

        Returns
        -------
        array_like
            Values of PDF evaluated in `x`.
        """
        warnings.warn("Function 'density' is deprecated. Use 'pdf' instead.")
        return self.pdf(x)


def assign_sampler(param):
    """ Assign a univariate sampler to the given parameter.

    Parameters
    ----------
    param : pythia.parameter.RandomParameter

    Returns
    -------
    pythia.sampler.Sampler
        Univariate sampler.
    """
    distDict = pt.misc.distributionDict()
    if param.distribution in distDict['uniform']:
        return UniformSampler(param.domain)
    elif param.distribution in distDict['normal']:
        return NormalSampler(param.mean, param.variance)
    elif param.distribution in distDict['gamma']:
        return GammaSampler(param.domain, param.alpha, param.beta)
    elif param.distribution in distDict['beta']:
        return BetaSampler(param.domain, param.alpha, param.beta)
    else:
        raise ValueError('unknown distribution: {}'.format(param.distribution))


def get_maximum(f, domain, nPoints=1000):
    """ Compute essential maximum of function by point evaluations.

    Parameters
    ----------
    f : function
        Function to evaluate. Needs to map from n-dim space to 1-dim space.
    domain : array_like
        Domain to evaluate function on.
    nPoints : int, default=1000
        Number of function evaluations. Evaluations are done on a uniform grid
        in domain. Actual number of points may thus be a little greater.

    Returns
    -------
    float
        Approximation of maximum of function `f`.
    """
    doms = np.array(domain)
    assert doms.shape[-1] == 2 and doms.ndim == 2
    nDimPoints = int(np.ceil(np.power(nPoints, 1/domain.shape[0])))
    if doms.shape[0] > 1:
        eps = np.finfo(float).eps  # circumvent inf on bdry
        x = pt.misc.cartProd([
            np.linspace(dom[0]+eps, dom[1]-eps, nDimPoints) for dom in doms]
        )
    else:
        x = np.linspace(*doms[0], nDimPoints).reshape(-1, 1)
    return np.max(abs(f(x)))


if __name__ == "__main__":
    pass
