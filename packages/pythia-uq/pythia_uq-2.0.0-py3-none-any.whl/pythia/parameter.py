""" PyThia classes containing Parameter information. """
import numpy as np


class Parameter(object):
    """ Basic parameter with fixed value.

    Parameters
    ----------
    name : str
        Name identifier of the parameter.
    value : float, optional
        Parameter value.
    """
    # TODO(Nando): Attributes should not be properties.

    def __init__(self, name, value=None):
        """ Initialize parameter object. """
        self._name = name
        assert isinstance(self._name, str)
        self._val = value
        self._mode = 'fixed'

    @property
    def name(self):
        """ Parameter name. """
        return self._name

    @property
    def value(self):
        """ Parameter value. """
        return self._val

    @value.setter
    def value(self, value):
        """ Set parameter value.

        Parameters
        ----------
        value : float
            Parameter value.
        """
        self._val = value

    @property
    def mode(self):
        """ Type (mode) of parameter. """
        return self._mode

    def __repr__(self):
        frmttr = '{:<5} : {}\n'
        text = ''
        text += frmttr.format('name', self.name)
        text += frmttr.format('value', self.value)
        text += frmttr.format('mode', self.mode)
        return text[:-1]


class SteadyParameter(Parameter):
    """ Subclass of Parameter used for deterministic parameter variations.

    Parameter representing part of the spatial/physical domain of the problem.

    Parameters
    ----------
    name : str
        Parameter name.
    value : array_like
        Values the parameter is iterated over.
    index : int, optional
        Enumeration index of the parameter. Set automatically if `None`.
    """
    # TODO(Nando): Attributes should not be properties.

    _index = 0

    def __init__(self, name, value, index=None):
        """ Initialize SteadyParameter object. """
        if index is None:
            self._idx = int(SteadyParameter._index)
            SteadyParameter._index += 1
        else:
            self._idx = index

        self._name = name
        assert isinstance(self._name, str)
        self._val = value
        assert hasattr(self._val, '__iter__')
        self._mode = 'discrete'

    @property
    def name(self):
        """ Parameter name. """
        return self._name

    @property
    def index(self):
        """ Index of the parameter. """
        return self._idx

    @property
    def value(self):
        """ Parameter value. """
        return self._val

    @value.setter
    def value(self, value):
        """ Set parameter value.

        Parameters
        ----------
        value : array_like
            Parameter values.
        """
        self._val = value
        assert hasattr(self._val, '__iter__')

    def __repr__(self):
        frmttr = '{:<8} : {}\n'
        text = ''
        text += frmttr.format('name', self.name)
        text += frmttr.format('index', self.index)
        text += frmttr.format('mode', self.mode)
        text += frmttr.format('value', self.value)
        return text[:-1]


class RandomParameter(Parameter):
    """ Subclass of Parameter used for stochasic parameters.

    Parameters
    ----------
    name : str
        Parameter name.
    domain : array_like
        Supported domain of the parameter distribution.
    distribution : str
        Distribution identifier of the parameter.
    value : float or array_like, optional
        Value (expected) of the parameter. Only used to store information never
        required for computations.
    index : int, optional
        Enumeration index of the parameter. Set automatically if `None`.
    """
    # TODO(Nando): Attributes should not be properties.

    _index = 0

    def __init__(self, name, domain, distribution, value=None, index=None):
        """ Initialize RandomParameter object. """
        if index is None:
            self._idx = int(RandomParameter._index)
            RandomParameter._index += 1
        else:
            self._idx = index

        self._name = name
        assert isinstance(self._name, str)
        self._dom = np.array(domain)
        assert self._dom.shape == (2,)
        self._dist = distribution
        assert isinstance(self._dist, str)
        self._val = value
        self._mode = 'continuous'
        self._alpha, self._beta = None, None
        self._mean, self._var = None, None

    @property
    def index(self):
        """ Index of the parameter. """
        return self._idx

    @property
    def domain(self):
        """ Supported domain of the parameter. """
        return self._dom

    @domain.setter
    def domain(self, domain):
        """ Set parameter domain.

        Parameters
        ----------
        domain : array_like
            Parameter domain (interval).
        """
        self._dom = domain
        assert self._dom.shape == (2,)

    @property
    def distribution(self):
        """ Distribution identifier of the parameter. """
        return self._dist

    @property
    def alpha(self):
        """ Parameter required for Beta or Gamma distribution. """
        return self._alpha

    @alpha.setter
    def alpha(self, alpha):
        """ Set parameter (DoF) for Beta or Gamma distribution.

        Parameters
        ----------
        alpha : float
        """
        self._alpha = float(alpha)
        assert self._alpha > 0

    @property
    def beta(self):
        """ Parameter required for Beta distribution. """
        return self._beta

    @beta.setter
    def beta(self, beta):
        """ Set parameter (DoF) for Beta distribution.

        Parameters
        ----------
        beta : float
        """
        self._beta = float(beta)
        assert self._beta > 0

    @property
    def mean(self):
        """ Mean of parameter distribution. """
        return self._mean

    @mean.setter
    def mean(self, mean):
        """ Set parameter distribution mean for normal distribution.

        Parameters
        ----------
        mean : float
        """
        self._mean = float(mean)

    @property
    def variance(self):
        """ Variance of parameter distribution. """
        return self._var

    @variance.setter
    def variance(self, var):
        """ Set parameter distribution variance for normal distribution.

        Parameters
        ----------
        var : float
        """
        self._var = float(var)
        assert var >= 0

    def __repr__(self):
        frmttr = '{:<8} : {}\n'
        text = ''
        text += frmttr.format('name', self.name)
        text += frmttr.format('index', self.index)
        text += frmttr.format('domain', self.domain)
        text += frmttr.format('mode', self.mode)
        text += frmttr.format('dist', self.distribution)
        if self.alpha is not None:
            text += frmttr.format('alpha', self.alpha)
        if self.beta is not None:
            text += frmttr.format('beta', self.beta)
        if self.mean is not None:
            text += frmttr.format('mean', self.mean)
        if self.variance is not None:
            text += frmttr.format('variance', self.variance)
        text += frmttr.format('value', self.value)
        return text[:-1]


if __name__ == '__main__':
    pass
