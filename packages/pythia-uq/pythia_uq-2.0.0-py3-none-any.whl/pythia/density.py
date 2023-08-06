""" Assemble univariate and multivariate PDFs for stochastic parameters.

Build the univariate and multivariate probability density functions (PDFs)
for `pythia.parameter.RandomParameter` parameters.
"""
import numpy as np
import scipy.stats
import pythia as pt


def paramPDF(params):
    """ Set the PDF for each parameter according to the parameter distribution.

    The PDF of parameter `j` can be evaluated at some point
    :math:`x\\in\\mathbb{R}` by `pdf[j](x)`.

    Parameters
    ----------
    params : list of `pythia.parameters.RandomParameter`
        List of parameters with information of the probability distribution.

    Returns
    -------
    pdf : list of function
        List of univariate PDFs for each parameter.
    """

    pdf = [None]*len(params)
    distDict = pt.misc.distributionDict()

    for jj, param in enumerate(params):

        if param.distribution in distDict['uniform']:  # uniform distribution
            def density(x, param=param):
                a, b = param.domain
                # uniform pdf f(x) for x in [a,b]
                return scipy.stats.uniform.pdf(x, loc=a, scale=b-a)
        elif param.distribution in distDict['normal']:  # normal distribution
            def density(x, param=param):
                mean, dev = param.mean, np.sqrt(param.variance)
                # Gaussian pdf f(x,mu,sigma) for x in (-Inf, Inf)
                return scipy.stats.norm.pdf(x, loc=mean, scale=dev)
        elif param.distribution in distDict['gamma']:  # gamma distribution
            def density(x, param=param):
                alpha, beta = param.alpha, param.beta
                # Rescale Gamma distribution from [0,inf) to [a,inf).
                a = param.domain[0]
                y = x - a
                # Gamma pdf f(x,alpha,beta) for x in [a, inf)
                return scipy.stats.gamma.pdf(y, a=alpha, scale=1.0/beta)
        elif param.distribution in distDict['beta']:  # beta distribution
            def density(x, param=param):
                alpha, beta = param.alpha, param.beta
                # Rescale Beta distribution from [0,1] to param.domain.
                a, b = param.domain
                y = pt.misc.shiftCoord(x, [a, b], [0, 1])
                # Beta pdf f(x,alpha,beta) for x in [a, b]
                return scipy.stats.beta.pdf(y, a=alpha, b=beta)/(b-a)
        else:
            raise NotImplementedError(
                f"unknown distribution '{param.distribution}'")

        pdf[jj] = density
    return pdf


def multivariatePDF(uPDF):
    """ Compute the multivariate (product) PDF of the given parameters.

    Parameters
    ----------
    uPDF : list of function
        List of univariate PDFs.

    Returns
    -------
    pdf : function
        Multivariate parameter PDF.
    """
    def pdf(p):
        if not 0 < p.ndim < 3:
            raise ValueError(f"Wrong ndim: {p.ndim}")
        if p.ndim == 1:
            p.shape = 1, -1
        val = np.empty(p.shape)
        for jj in range(p.shape[1]):
            val[:, jj] = uPDF[jj](p[:, jj])
        return np.prod(val, axis=1)
    return pdf


if __name__ == "__main__":
    pass
