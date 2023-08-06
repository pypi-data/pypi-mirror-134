import numpy as np
import warnings
import pythia as pt


def random_walk_metropolis(density, domain, seeds, CHAIN_LENGTH, DELTA):
    """ Random walk Metropolis-Hastings algorithm for sampling densities.

    Since the random walks for multiple seeds are computed in parallel, the
    seed length of each seed is chosen uniformly.

    .. deprecated:: 2.0.0
        This is just for benchmarking MCMC sampling. Use other python libraries
        for reasonable computations.

    Parameters
    ----------
    density : function
        Density (not necessarily normalized) from which the samples are
        generated.
    seeds : array_like, ndim = 2
        Seed for stochastic sampling. First dimension is the number of seeds
        used for parallel sampling, second dimension is the dimension of the
        samples/parameters.
    CHAIN_LENGTH : int
        Length of the Markov chains.
    DELTA : array_like
        Standart deviation of noise direction added in each step for each
        parameter.

    """
    warnings.warn("Depretiated legacy code. External sampling preferred.")
    if seeds.ndim < 2:
        seeds.shape = 1, -1
    assert seeds.ndim == 2
    N_SEEDS, DIM = seeds.shape

    val = np.zeros([CHAIN_LENGTH, N_SEEDS, DIM])
    val[0] = seeds
    REJECTIONS = np.zeros(N_SEEDS)
    THRESHOLD = np.random.uniform(0, 1, [CHAIN_LENGTH, N_SEEDS])
    x = density(val[0])
    perturbation = np.zeros([N_SEEDS, DIM])

    # NOTE start with j=1 since val[0] is seed!
    for j in range(1, CHAIN_LENGTH):
        for j_seed in range(N_SEEDS):
            while True:
                EPS = np.random.normal(0, DELTA)
                perturbation[j_seed] = val[j-1, j_seed] + EPS
                if pt.misc.is_contained(perturbation[j_seed], domain):
                    break
        y = density(perturbation)
        for j_seed in range(N_SEEDS):
            # alpha = y[j_seed] / x[j_seed] if x[j_seed] > 0 else 1
            if THRESHOLD[j, j_seed]*x[j_seed] <= y[j_seed]:
                val[j, j_seed] = perturbation[j_seed]
                x[j_seed] = y[j_seed]
            else:
                REJECTIONS[j_seed] += 1
                val[j, j_seed] = val[j-1, j_seed]

    return val.swapaxes(0, 1), REJECTIONS
