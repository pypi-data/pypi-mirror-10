import numpy as np

import param

from ..core import util
from ..core import OrderedDict, Dimension, NdMapping, Element2D, NdElement, HoloMap
from .tabular import ItemTable, Table


class Chart(Element2D):
    """
    The data held within an Array is a numpy array of shape (n, m).
    Element2D objects are sliceable along the X dimension allowing easy
    selection of subsets of the data.
    """

    key_dimensions = param.List(default=[Dimension('x')], bounds=(1,2), doc="""
        Dimensions on Element2Ds determine the number of indexable
        dimensions.""")

    group = param.String(default='Chart', constant=True)

    value_dimensions = param.List(default=[Dimension('y')], bounds=(1,3), doc="""
        Dimensions on Element2Ds determine the number of indexable
        dimensions.""")

    _null_value = np.array([[], []]).T # For when data is None

    def __init__(self, data, **params):
        settings = {}
        if isinstance(data, Chart):
            settings = dict(data.get_param_values(onlychanged=True))
            data = data.data
        elif isinstance(data, NdMapping) or (isinstance(data, list) and data
                                           and isinstance(data[0], Element2D)):
            data, settings = self._process_map(data)
        data = list(data)
        data = self._null_value if (data is None) or (len(data) == 0) else data
        if len(data) and not isinstance(data, np.ndarray):
            data = np.array(data)

        settings.update(params)
        super(Chart, self).__init__(data, **settings)
        self.data = self._validate_data(data)


    def _validate_data(self, data):
        if data.ndim > 1 and not data.shape[1] == len(self.dimensions()):
            raise ValueError("Data has to match number of key and value dimensions")
        return data

    def _process_map(self, ndmap):
        """
        Base class to process an NdMapping to be collapsed into a Chart.
        Should return the data and parameters of the new Chart.
        """
        if isinstance(ndmap, Table):
            data = np.vstack([np.concatenate([key, vals])
                              for key, vals in ndmap.data.items()]).astype(np.float)
            settings = dict(ndmap.get_param_values(onlychanged=True))
        else:
            data = np.concatenate([v.data for v in ndmap])
            settings = dict([v for v in ndmap][0].get_param_values(onlychanged=True))
        return data, settings


    def closest(self, coords):
        """
        Given single or multiple x-values, returns the list
        of closest actual samples.
        """
        if not isinstance(coords, list): coords = [coords]
        xs = self.data[:, 0]
        idxs = [np.argmin(xs-coord) for coord in coords]
        return [xs[idx] for idx in idxs]


    def __getitem__(self, slices):
        """
        Implements slicing or indexing of the data by the data x-value.
        If a single element is indexed reduces the Element2D to a single
        Scatter object.
        """
        if slices is ():
            return self
        if not isinstance(slices, tuple): slices = (slices,)
        if len(slices) > self.ndims:
            raise Exception("Slice must match number of key_dimensions.")

        data = self.data
        lower_bounds, upper_bounds = [], []
        for idx, slc in enumerate(slices):
            if isinstance(slc, slice):
                start = slc.start if slc.start else -float("inf")
                stop = slc.stop if slc.stop else float("inf")

                clip_start = start <= data[:, idx]
                clip_stop = data[:, idx] < stop
                data = data[np.logical_and(clip_start, clip_stop), :]
                lbound = self.extents[idx]
                ubound = self.extents[self.ndims:][idx]
                lower_bounds.append(lbound if slc.start is None else slc.start)
                upper_bounds.append(ubound if slc.stop is None else slc.stop)
            else:
                data_index = data[:, idx] == slc
                if not any(data_index):
                    raise IndexError("Value %s not found in data." % slc)
                data = data[data_index, :]
        if not any(isinstance(slc, slice) for slc in slices):
            data = data[:, self.ndims:]
            return data[0] if data.shape[1] == 1 else data
        if self.ndims == 1:
            lower_bounds.append(None)
            upper_bounds.append(None)

        return self.clone(data, extents=tuple(lower_bounds + upper_bounds))


    @classmethod
    def collapse_data(cls, data, function, **kwargs):
        new_data = [arr[:, 1:] for arr in data]
        if isinstance(function, np.ufunc):
            collapsed = function.reduce(new_data)
        else:
            collapsed = function(np.dstack(new_data), axis=-1, **kwargs)
        return np.hstack([data[0][:, 0, np.newaxis], collapsed])


    def sample(self, samples=[]):
        """
        Allows sampling of Element2D objects using the default
        syntax of providing a map of dimensions and sample pairs.
        """
        sample_data = OrderedDict()
        for sample in samples:
            data = self[sample]
            data = data if np.isscalar(data) else tuple(data)
            sample_data[sample] = data
        params = dict(self.get_param_values(onlychanged=True))
        params.pop('extents', None)
        return Table(sample_data, **dict(params, key_dimensions=self.key_dimensions,
                                         value_dimensions=self.value_dimensions))


    def reduce(self, dimensions=[], function=None, **reduce_map):
        """
        Allows collapsing of Chart objects using the supplied map of
        dimensions and reduce functions.
        """
        dimensions = self._valid_dimensions(dimensions)
        if dimensions and reduce_map:
            raise Exception("Pass reduced dimensions either as an argument"
                            "or as part of the kwargs not both.")
        elif dimensions:
            reduce_map = {dimensions[0]: function}
        elif not reduce_map:
            reduce_map = {d: function for d in self._cached_index_names}

        if len(reduce_map) > 1:
            raise ValueError("Chart Elements may only be reduced to a point.")
        dim, reduce_fn = list(reduce_map.items())[0]
        if dim in self._cached_index_names:
            reduced_data = OrderedDict(zip(self.value_dimensions, reduce_fn(self.data[:, self.ndims:], axis=0)))
        else:
            raise Exception("Dimension %s not found in %s" % (dim, type(self).__name__))
        params = dict(self.get_param_values(onlychanged=True), value_dimensions=self.value_dimensions,
                      key_dimensions=[])
        params.pop('extents', None)
        return ItemTable(reduced_data, **params)


    def __len__(self):
        return len(self.data)


    def dimension_values(self, dim):
        index = self.get_dimension_index(dim)
        if index < len(self.dimensions()):
            return self.data[:, index]
        else:
            return super(Chart, self).dimension_values(dim)


    def range(self, dim, data_range=True):
        dim_idx = dim if isinstance(dim, int) else self.get_dimension_index(dim)
        dim = self.get_dimension(dim_idx)
        if dim.range != (None, None):
            return dim.range
        elif dim_idx < len(self.dimensions()):
            if self.data.ndim == 1:
                data = np.atleast_2d(self.data).T
            else:
                data = self.data
            if len(data):
                data = data[:, dim_idx]
                data_range = np.nanmin(data), np.nanmax(data)
            else:
                data_range = (np.NaN, np.NaN)
        if data_range:
            return util.max_range([data_range, dim.soft_range])
        else:
            return dim.soft_range


    def dframe(self):
        import pandas as pd
        columns = [d.name for d in self.dimensions()]
        return pd.DataFrame(self.data, columns=columns)



class Scatter(Chart):
    """
    Scatter is a Element2D type which gets displayed as a number of
    disconnected points.
    """

    group = param.String(default='Scatter', constant=True)

    @classmethod
    def collapse_data(cls, data, function=None, **kwargs):
        if function:
            raise Exception("Scatter elements are inhomogenous and "
                            "cannot be collapsed with a function.")
        return np.concatenate(data)


class Curve(Chart):
    """
    Curve is a simple Chart Element providing 1D indexing along
    the x-axis.
    """

    group = param.String(default='Curve', constant=True)

    def progressive(self):
        """
        Create map indexed by Curve x-axis with progressively expanding number
        of curve samples.
        """
        vmap = HoloMap(None, key_dimensions=self.key_dimensions,
                       title=self.title+' {dims}')
        for idx in range(len(self.data)):
            x = self.data[0]
            if x in vmap:
                vmap[x].data.append(self.data[0:idx])
            else:
                vmap[x] = self.clone(self.data[0:idx])
        return vmap



class ErrorBars(Chart):
    """
    ErrorBars is a Chart Element type representing any number of
    errorbars situated in a 2D space. The errors must be supplied
    as an Nx3 or Nx4 array representing the x/y-positions and
    either the symmetric error or assymetric errors respectively.
    Internally the data is always held as an Nx4 array with the
    lower and upper bounds.
    """

    group = param.String(default='ErrorBars', constant=True, doc="""
        A string describing the quantitity measured by the ErrorBars
        object.""")

    key_dimensions = param.List(default=[Dimension('x'), Dimension('y')],
                                bounds=(2, 2), constant=True, doc="""
        The Dimensions corresponding to the x- and y-positions of
        the error bars.""")

    value_dimensions = param.List(default=[Dimension('lerror'), Dimension('uerror')],
                                  bounds=(2,2), constant=True)

    def __init__(self, data, **params):
        data = list(data)
        data = self._null_value if (data is None) or (len(data) == 0) else data
        if len(data) and not isinstance(data, np.ndarray):
            data = np.array(data)
        if data.shape[1] == 3:
            data = np.hstack([data, np.atleast_2d(data[:, 2]).T])
        super(ErrorBars, self).__init__(data, **params)



class Bars(NdElement):
    """
    Bars is an Element type, representing a number of stacked and
    grouped bars, depending the dimensionality of the key and value
    dimensions. Bars is useful for categorical data, which may be
    laid via groups, categories and stacks. Internally Bars is
    a NdElement with up to three key dimensions and a single value
    dimension.
    """

    group = param.String(default='Bars', constant=True)

    key_dimensions = param.List(default=[Dimension('x')], bounds=(1,3))

    value_dimensions = param.List(default=[Dimension('y')], bounds=(1,1))



class Histogram(Element2D):
    """
    Histogram contains a number of bins, which are defined by the
    upper and lower bounds of their edges and the computed bin values.
    """

    key_dimensions = param.List(default=[Dimension('x')], bounds=(1,1), doc="""
        Dimensions on Element2Ds determine the number of indexable
        dimensions.""")

    group = param.String(default='Histogram', constant=True)

    value_dimensions = param.List(default=[Dimension('Frequency')])

    def __init__(self, values, edges=None, extents=None, **params):
        self.values, self.edges, settings = self._process_data(values, edges)
        settings.update(params)
        super(Histogram, self).__init__((self.values, self.edges), **settings)
        self._width = None
        self._extents = (None, None, None, None) if extents is None else extents


    def __getitem__(self, key):
        """
        Implements slicing or indexing of the Histogram
        """
        if key is (): return self # May no longer be necessary
        if isinstance(key, tuple) and len(key) > self.ndims:
            raise Exception("Slice must match number of key_dimensions.")

        centers = [(float(l)+r)/2 for (l,r) in zip(self.edges, self.edges[1:])]
        if isinstance(key, slice):
            start, stop = key.start, key.stop
            if [start, stop] == [None,None]: return self
            start_idx, stop_idx = None,None
            if start is not None:
                start_idx = np.digitize([start], centers, right=True)[0]
            if stop is not None:
                stop_idx = np.digitize([stop], centers, right=True)[0]

            slice_end = stop_idx+1 if stop_idx is not None else None
            slice_values = self.values[start_idx:stop_idx]
            slice_edges =  self.edges[start_idx: slice_end]

            extents = (min(slice_edges), self.extents[1],
                       max(slice_edges), self.extents[3])
            return self.clone((slice_values, slice_edges), extents=extents)
        else:
            if not (self.edges.min() <= key < self.edges.max()):
                raise Exception("Key value %s is out of the histogram bounds" % key)
            idx = np.digitize([key], self.edges)[0]
            return self.values[idx-1 if idx>0 else idx]



    def _process_data(self, values, edges):
        """
        Ensure that edges are specified as left and right edges of the
        histogram bins rather than bin centers.
        """
        settings = {}
        (values, edges) = values if isinstance(values, tuple) else (values, edges)
        if isinstance(values, Element2D):
            values = values.data[:, 0]
            edges = values.data[:, 1]
            settings = dict(values.get_param_values(onlychanged=True))
        elif isinstance(values, np.ndarray) and len(values.shape) == 2:
            values = values[:, 0]
            edges = values[:, 1]
        elif all(isinstance(el, tuple) for el in values):
            edges, values = zip(*values)
        else:
            values = np.array(values)
            edges = np.array(edges, dtype=np.float)

        if len(edges) == len(values):
            widths = list(set(np.diff(edges)))
            if len(widths) == 1:
                width = widths[0]
            else:
                raise Exception('Centered bins have to be of equal width.')
            edges -= width/2.
            edges = np.concatenate([edges, [edges[-1]+width]])
        return values, edges, settings


    @property
    def extents(self):
        if any(lim is not None for lim in self._extents):
            return self._extents
        else:
            return (np.min(self.edges), None, np.max(self.edges), None)


    @extents.setter
    def extents(self, extents):
        self._extents = extents


    def dimension_values(self, dim):
        if isinstance(dim, int):
            dim = self.get_dimension(dim).name
        if dim in self._cached_value_names:
            return self.values
        elif dim in self._cached_index_names:
            return np.convolve(self.edges, np.ones((2,))/2, mode='valid')
        else:
            return super(Histogram, self).dimension_values(dim)


    def sample(self, **samples):
        raise NotImplementedError('Cannot sample a Histogram.')


    def reduce(self, dimensions=None, function=None, **reduce_map):
        raise NotImplementedError('Reduction of Histogram not implemented.')



class Points(Chart):
    """
    Allows sets of points to be positioned over a sheet coordinate
    system. Each points may optionally be associated with a chosen
    numeric value.

    The input data can be a Nx2 or Nx3 Numpy array where the first two
    columns corresponds to the X,Y coordinates in sheet coordinates,
    within the declared bounding region. For Nx3 arrays, the third
    column corresponds to the magnitude values of the points. Any
    additional columns will be ignored (use VectorFields instead).

    The input data may be also be passed as a tuple of elements that
    may be numpy arrays or values that can be cast to arrays. When
    such a tuple is supplied, the elements are joined column-wise into
    a single array, allowing the magnitudes to be easily supplied
    separately.

    Note that if magnitudes are to be rendered correctly by default,
    they should lie in the range [0,1].
    """

    key_dimensions = param.List(default=[Dimension('x'), Dimension('y')],
                                  bounds=(2, 2), constant=True, doc="""
        The label of the x- and y-dimension of the Points in form
        of a string or dimension object.""")

    group = param.String(default='Points', constant=True)

    value_dimensions = param.List(default=[], bounds=(0, 2))


    _min_dims = 2                      # Minimum number of columns

    def __len__(self):
        return self.data.shape[0]

    def __iter__(self):
        i = 0
        while i < len(self):
            yield tuple(self.data[i, ...])
            i += 1

    @classmethod
    def collapse_data(cls, data, function, **kwargs):
        return Scatter.collapse_data(data, function, **kwargs)


    def dimension_values(self, dim):
        if dim in [d.name for d in self.dimensions()]:
            dim_index = self.get_dimension_index(dim)
            if dim_index < self.data.shape[1]:
                return self.data[:, dim_index]
            else:
                return [np.NaN] * len(self)
        else:
            return super(Points, self).dimension_values(dim)



class VectorField(Points):
    """
    A VectorField contains is a collection of vectors where each
    vector has an associated position in sheet coordinates.

    The constructor of VectorField is similar to the constructor of
    Points: the input data can be an NxM Numpy array where the first
    two columns corresponds to the X,Y coordinates in sheet
    coordinates, within the declared bounding region. As with Points,
    the input can be a tuple of array objects or of objects that can
    be cast to arrays (the tuple elements are joined column-wise).

    The third column maps to the vector angle which must be specified
    in radians. Note that it is possible to supply a collection which
    isn't a numpy array, whereby each element of the collection is
    assumed to be an iterable corresponding to a single column of the
    NxM array.

    The visualization of any additional columns is decided by the
    plotting code. For instance, the fourth and fifth columns could
    correspond to arrow length and colour map value. All that is
    assumed is that these additional dimension are normalized between
    0.0 and 1.0 for the default visualization to work well.

    The only restriction is that the final data array is NxM where
    M>3. In other words, the vector must have a dimensionality of 2 or
    higher.
    """

    group = param.String(default='VectorField', constant=True)

    value_dimensions = param.List(default=[Dimension('Angle', cyclic=True, range=(0,2*np.pi)),
                                           Dimension('Magnitude')], bounds=(1, 2))

    _null_value = np.array([[], [], [], []]).T # For when data is None
    _min_dims = 3                              # Minimum number of columns

    def __init__(self, data, **params):
        if not isinstance(data, np.ndarray):
            data = np.array([
                [el for el in (col.flat if isinstance(col,np.ndarray) else col)]
                for col in data]).T
        super(VectorField, self).__init__(data, **params)
