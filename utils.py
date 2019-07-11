"""
utility functions and classes
"""

import numpy as np


class packarray(np.ndarray):
    """ 
    A packarray packs/copies several arrays into the same memory chunk.
    It feels like a list of arrays, but because the memory chunk is continuous,
    arithmatic operations are easier to use(via packarray)
    """
    def __new__(cls, array, start=None, end=None):
        """ 
        if end is none, start contains the sizes.
        if start is also none, array is a list of arrays to concatenate
        """
        self = array.view(type=cls)
        if end is None and start is None:
            start = np.array([len(arr) for arr in array], dtype='intp')
            array = np.concatenate(array)
        if end is None:
            sizes = start
            self.start = np.zeros(shape=len(sizes), dtype='intp')
            self.end = np.zeros(shape=len(sizes), dtype='intp')
            self.end[:] = sizes.cumsum()
            self.start[1:] = self.end[:-1]
        else:
            self.start = start
            self.end = end
            self.A = array
        return self

    @classmethod
    def adapt(cls, source, template):
        """ 
        adapt source to a packarray according to the layout of template 
        """
        if not isinstance(template, packarray):
            raise TypeError('template must be a packarray')
        return cls(source, template.start, template.end)

    def __repr__(self):
        return 'packarray: %s, start=%s, end=%s' % \
               (repr(self.A),
               repr(self.start), repr(self.end))
  
    def __str__(self):
        return repr(self)

    def copy(self):
        return packarray(self.A.copy(), self.start, self.end)

    def compress(self, mask):
        count = self.end - self.start
        realmask = np.repeat(mask, count)
        return packarray(self.A[realmask], self.start[mask], self.end[mask])

    def __getitem__(self, index):
        if isinstance(index, basestring):
            return packarray(self.A[index], self.end - self.start)

        if isinstance(index, slice) :
            start, end, step = index.indices(len(self))
        
            if step == 1:
                return packarray(self.A[self.start[start]:self.end[end]],
                    self.start[start:end] - self.start[start],
                    self.end[start:end] - self.start[start])

        if isinstance(index, (list, np.ndarray)):
            return packarray(self.A, self.start[index], self.end[index])

        if np.isscalar(index):
            start, end = self.start[index], self.end[index]
            if end > start: return self.A[start:end]
            else: return np.empty(0, dtype=self.A.dtype)
        
        raise IndexError('unsupported index type %s' % type(index))

    def __len__(self):
        return len(self.start)

    def __iter__(self):
        for i in range(len(self.start)):
            yield self[i]

    def __reduce__(self):
        return packarray, (self.A, self.end - self.start)

    def __array_wrap__(self, outarr, context=None):
        return packarray.adapt(outarr.view(np.ndarray), self)