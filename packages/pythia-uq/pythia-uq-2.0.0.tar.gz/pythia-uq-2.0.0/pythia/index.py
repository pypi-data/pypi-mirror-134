""" Store information about sparse multiindices.

Provide information about sparse PC expansion terms in form of multiindices
of polynomial degrees for each of the parameter dimensions. Also compute
Sobol indices subscripts and provide conversions of PC multiindices (mdx)
Sobol multiindices (sdx) and linear enumeration (idx).
"""
import numpy as np
import itertools
import pythia as pt


class PCMultiIndex(object):
    """ Generate multiindices for sparse PC expansion.

    Parameters
    ----------
    dimension : int
        Number of stochastic parameters.
    """
    # TODO(Nando): Attributes should not be extra properties!

    def __init__(self, dimension):
        """ Initialize empty sparse multiindex object. """
        self._dim = dimension
        self._count, self._sorted = 0, False
        self._max = -1*np.ones([1, self._dim], dtype=int)
        self._mdx, self._sdx = None, None
        self._mdx2sdx, self._sdx2mdx, self._mdx2idx = None, None, None

    @property
    def maximum(self):
        """ Maximum univariate polynomial degree. """
        if np.sum(self._max) < 0:
            return None
        return self._max

    @property
    def dimension(self):
        """ Number of stochastic parameters. """
        return self._dim

    @property
    def count(self):
        """ Number of PC expansion terms. """
        return self._count

    @property
    def mdx(self):
        """ Array of PC expansion multiindices.  """
        return self._mdx

    @property
    def sdx(self):
        """ List of Sobol indices subscripts. """
        return self._sdx

    @property
    def mdx2sdx(self):
        """ Dictionary to map mdx to corresponding sdx. """
        return self._mdx2sdx

    @property
    def sdx2mdx(self):
        """ Dictionary to map sdx to all corresponding mdx. """
        return self._sdx2mdx

    @property
    def mdx2idx(self):
        """ Dictionary to map mdx to enumeration index. """
        return self._mdx2idx

    @mdx.setter
    def mdx(self, mdx):
        """ Set multiindices.

        Parameters
        ----------
        mdx : array_like
            Array of multiindices. Shape is number of multiindices times
            parameter dimension.
        """
        self._mdx = mdx
        assert mdx.shape[1] == self.dimension
        self._count = self._mdx.shape[0]
        self._max = np.max(self._mdx, axis=0)

    @sdx.setter
    def sdx(self, sdx):
        """ Set Sobol indices subscripts.

        Parameters
        ----------
        sdx : list of tuple
            List of Sobol indices subscripts.
        """
        self._sdx = sdx

    @mdx2sdx.setter
    def mdx2sdx(self, mdx2sdx):
        """ Set dictionary to map PC multiindices to Sobol indices subscripts.

        Parameters
        ----------
        mdx2sdx : dict
        """
        self._mdx2sdx = mdx2sdx

    @sdx2mdx.setter
    def sdx2mdx(self, sdx2mdx):
        """ Set dictionary to map Sobol indices subscripts to PC multiindices.

        Parameters
        ----------
        sdx2mdx : dict
        """
        self._sdx2mdx = sdx2mdx

    @mdx2idx.setter
    def mdx2idx(self, mdx2idx):
        """ Set dictionary to map PC multiindices to enumeration index.

        Parameters
        ----------
        mdx2idx : dict
        """
        self._mdx2idx = mdx2idx

    def refresh(self):
        """ Generate Sobol indices and index dictionaries from `mdx` array. """
        self.sdx = self.generateSDX()
        self.mdx2sdx = self.generateMDX2SDX()
        self.sdx2mdx = self.generateSDX2MDX()
        self.mdx2idx = self.generateMDX2IDX()
        self.sdx2idx = self.generateSDX2IDX()

    def mdxSort(self, mdx):
        """ Sort mdx by sum.

        Parameters
        ----------
        mdx : array_like
            Array of PC multiindices.
        """
        sortIdx = np.argsort(np.sum(mdx, axis=1))
        return mdx[sortIdx], sortIdx

    def mdxFromShape(self, shape):
        """ Compute (full tensor) multiindices up to specified degree.

        Parameters
        ----------
        shape : iterable
            Maximal indices for multiindex.
        """
        # Create array with multi-indices in each row.
        mdx = [np.arange(jShape+1) for jShape in shape]
        if len(shape) > 1:
            mdx = pt.misc.cartProd(mdx)
        else:
            mdx = np.array(mdx).T
        return self.mdxSort(mdx)[0]

    def mdxLimitAbs(self, limit):
        """ Limit maximal dimension of multiindices.

        Restrict `self.mdx` to a sub-array of multiindices with total degree
        less or equal to the specified limit.

        Parameters
        ----------
        limit : int
            Limit for the total degree of the multiindices.
        """
        assert isinstance(limit, int)
        self.mdx = self.mdx[np.sum(self.mdx, axis=1) <= limit]
        self._maxAbs = limit

    def mdxAdd(self, pos, deg):
        """ Assemble array of multiindices as cartesian product of deg in pos.

        Parameters
        ----------
        pos : list
            Positions where multiindices are added.
        deg : list of lists
            Multiindex values for position of same length as `pos`.

        Returns
        -------
        array_like
            Sorted array of PC multiindices.
        """
        assert len(deg) == len(pos)
        if len(pos) > 1:
            c = pt.misc.cartProd(deg)
        else:
            c = np.array(deg).reshape(-1, 1)
        mdx = np.zeros([c.shape[0], self._dim])
        mdx[:, pos] = c
        if not self._mdx is None:
            mdx = np.concatenate([self._mdx, mdx], axis=0)
        return self.mdxSort(np.unique(mdx, axis=0))[0].astype(int)

    def generateSDX(self):
        """ Generate Sobol index subscripts for parameter dimension. """
        sdx = []
        for r in range(1, self.dimension+1):
            sdx += list(itertools.combinations(range(1, self.dimension+1), r))
        return sdx

    def generateMDX2SDX(self):
        """ Generate dictionary to map `mdx` to `sdx`.

        Generate dictionary with structre `dct[tuple(mdx)] = sdx`.

        .. note::
            The `mdx` are numpy ndarrays which cannot be cast to keys in python
            dictionaries. Hence the individual multiindices need to be cast to
            tuples before using the dictionary.
        """
        mdx2sdx = {
            tuple(idx): tuple(np.flatnonzero(idx)+1) for idx in self._mdx
        }
        return mdx2sdx

    def generateSDX2MDX(self):
        """ Generate dictionary to map `sdx` to all corresponding `mdx`. """
        sdx2mdx = {sdx: [] for sdx in self.sdx}
        for idx in self.mdx:
            sdx = tuple(np.flatnonzero(np.array(idx))+1)  # corresponding sdx
            if any(sdx):
                sdx2mdx[sdx].append(idx)
        for s in sdx2mdx.keys():
            sdx2mdx[s] = np.array(sdx2mdx[s])
        return sdx2mdx

    def generateMDX2IDX(self):
        """ Generate dict to map `tuple(mdx)` to corresponding index. """
        return dict(zip(list(map(tuple, self._mdx)), range(self._count)))

    def generateSDX2IDX(self):
        """ Generate dict to map `tuple(sdx)` to corresponding index. """
        return dict(zip(list(map(tuple, self._sdx)), range(len(self._sdx))))

    def __repr__(self):
        frmttr = '{:<3}    {:<7} : {:<}\n'
        text = ''
        text += frmttr.format('mdx', 'dim', self.dimension)
        text += frmttr.format('', 'count', self.count)
        text += frmttr.format('', 'dim max', str(self.maximum))
        if hasattr(self, '_maxAbs'):
            text += frmttr.format('', 'max abs', self._maxAbs)
        if bool(self.sdx):
            text += frmttr.format('sdx', 'count', len(self.sdx))
        return text[:-1]


if __name__ == "__main__":
    pass
