import copy
from itertools import product

import numpy as np
from matplotlib import pyplot as plt

import param

from ...core import CompositeOverlay, Element
from ...core import traversal
from ...core.util import match_spec, max_range
from ...element.raster import HeatMap, Image, Raster, RGB
from .element import ElementPlot, OverlayPlot
from .plot import MPLPlot, GridPlot


class RasterPlot(ElementPlot):

    aspect = param.Parameter(default='equal', doc="""
        Raster elements respect the aspect ratio of the
        Images by default but may be set to an explicit
        aspect ratio or to 'square'.""")

    colorbar = param.Boolean(default=False, doc="""
        Whether to add a colorbar to the plot.""")

    situate_axes = param.Boolean(default=False, doc="""
        Whether to situate the image relative to other plots. """)

    show_values = param.Boolean(default=False, doc="""
        Whether to annotate each pixel with its value.""")

    style_opts = ['alpha', 'cmap', 'interpolation', 'visible',
                  'filterrad', 'clims', 'norm']


    def __init__(self, *args, **kwargs):
        super(RasterPlot, self).__init__(*args, **kwargs)
        if self.map.type == Raster:
            self.invert_yaxis = not self.invert_yaxis


    def get_extents(self, view, ranges):
        extents = super(RasterPlot, self).get_extents(view, ranges)
        if self.situate_axes:
            return extents
        else:
            if isinstance(view, Image):
                return view.bounds.lbrt()
            else:
                return view.extents


    def initialize_plot(self, ranges=None):
        view = self.map.last
        axis = self.handles['axis']

        ranges = self.compute_ranges(self.map, self.keys[-1], ranges)
        ranges = match_spec(view, ranges)

        xticks, yticks = self._compute_ticks(view, ranges)

        opts = self.style[self.cyclic_index]
        data = view.data
        clims = opts.pop('clims', None)
        if view.depth != 1:
            opts.pop('cmap', None)

        if isinstance(view, Image):
            l, b, r, t = view.bounds.lbrt()
        else:
            l, b, r, t = view.extents
        if self.invert_yaxis and type(view) is Raster:
            b, t = t, b

        if isinstance(view, RGB):
            data = view.rgb.data
        elif isinstance(view, HeatMap):
            data = view.data
            data = np.ma.array(data, mask=np.logical_not(np.isfinite(data)))
            cmap_name = opts.pop('cmap', None)
            cmap = copy.copy(plt.cm.get_cmap('gray' if cmap_name is None else cmap_name))
            cmap.set_bad('w', 1.)
            opts['cmap'] = cmap

        im = axis.imshow(data, extent=[l, r, b, t], zorder=self.zorder, **opts)
        if clims is None:
            val_dim = [d.name for d in view.vdims][0]
            clims = ranges.get(val_dim)
        if 'norm' not in opts:
            im.set_clim(clims)
        self.handles['im'] = im
        if self.colorbar:
            self._draw_colorbar(im)

        if isinstance(view, HeatMap):
            self.handles['axis'].set_aspect(float(r - l)/(t-b))
            self.handles['annotations'] = {}

            if self.show_values:
                self._annotate_values(view)

        return self._finalize_axis(self.keys[-1], ranges=ranges,
                                   xticks=xticks, yticks=yticks)


    def _compute_ticks(self, view, ranges):
        if isinstance(view, HeatMap):
            xdim, ydim = view.kdims
            dim1_keys, dim2_keys = view.dense_keys()
            num_x, num_y = len(dim1_keys), len(dim2_keys)
            x0, y0, x1, y1 = view.extents
            xstep, ystep = ((x1-x0)/num_x, (y1-y0)/num_y)
            xpos = np.linspace(x0+xstep/2., x1-xstep/2., num_x)
            ypos = np.linspace(y0+ystep/2., y1-ystep/2., num_y)
            xlabels = [xdim.pprint_value(k) for k in dim1_keys]
            ylabels = [ydim.pprint_value(k) for k in dim2_keys]
            return (xpos, xlabels), (ypos, ylabels)
        else:
            return None, None


    def _annotate_values(self, view):
        axis = self.handles['axis']
        val_dim = view.vdims[0]
        dim1_keys, dim2_keys = view.dense_keys()
        num_x, num_y = len(dim1_keys), len(dim2_keys)
        xstep, ystep = 1.0/num_x, 1.0/num_y
        xpos = np.linspace(xstep/2., 1.0-xstep/2., num_x)
        ypos = np.linspace(ystep/2., 1.0-ystep/2., num_y)
        coords = product(dim1_keys, dim2_keys)
        plot_coords = product(xpos, ypos)
        for plot_coord, coord in zip(plot_coords, coords):
            if isinstance(view, HeatMap):
                val = view._data.get(coord, np.NaN)
                val = val[0] if isinstance(val, tuple) else val
            else:
                val = view[coord]
            val = val_dim.type(val) if val_dim.type else val
            val = val[0] if isinstance(val, tuple) else val
            text = val_dim.pprint_value(val)
            text = '' if val is np.nan else text
            if plot_coord not in self.handles['annotations']:
                annotation = axis.annotate(text, xy=plot_coord,
                                           xycoords='axes fraction',
                                           horizontalalignment='center',
                                           verticalalignment='center')
                self.handles['annotations'][plot_coord] = annotation
            else:
                self.handles['annotations'][plot_coord].set_text(text)
        old_coords = set(self.handles['annotations'].keys()) - set(product(xpos, ypos))
        for plot_coord in old_coords:
            annotation = self.handles['annotations'].pop(plot_coord)
            annotation.remove()


    def update_handles(self, axis, view, key, ranges=None):
        im = self.handles.get('im', None)
        im.set_data(view.data)

        if isinstance(view, HeatMap) and self.show_values:
           self._annotate_values(view)
        if self.colorbar:
            self._draw_colorbar(im)

        xdim, ydim = view.kdims
        if isinstance(view, Image):
            l, b, r, t = view.bounds.lbrt()
        else:
            l, b, r, t = view.extents
            if type(view) == Raster:
                b, t = t, b

        val_dim = [d.name for d in view.vdims][0]
        im.set_clim(ranges.get(val_dim))
        im.set_extent((l, r, b, t))
        xticks, yticks = self._compute_ticks(view, ranges)
        return {'xticks': xticks, 'yticks': yticks}



class RasterGridPlot(GridPlot, OverlayPlot):
    """
    RasterGridPlot evenly spaces out plots of individual projections on
    a grid, even when they differ in size. Since this class uses a single
    axis to generate all the individual plots it is much faster than the
    equivalent using subplots.
    """

    # Parameters inherited from OverlayPlot that are not part of the
    # GridPlot interface. Some of these may be enabled in future in
    # conjunction with GridPlot.

    apply_extents = param.Parameter(precedence=-1)
    apply_ranges = param.Parameter(precedence=-1)
    apply_ticks = param.Parameter(precedence=-1)
    bgcolor = param.Parameter(precedence=-1)
    invert_xaxis = param.Parameter(precedence=-1)
    invert_yaxis = param.Parameter(precedence=-1)
    legend_cols = param.Parameter(precedence=-1)
    legend_position = param.Parameter(precedence=-1)
    logx = param.Parameter(precedence=-1)
    logy = param.Parameter(precedence=-1)
    logz = param.Parameter(precedence=-1)
    orientation = param.Parameter(precedence=-1)
    show_grid = param.Parameter(precedence=-1)
    style_grouping = param.Parameter(precedence=-1)
    xticks = param.Parameter(precedence=-1)
    yticks = param.Parameter(precedence=-1)
    zticks = param.Parameter(precedence=-1)
    zaxis = param.Parameter(precedence=-1)
    zrotation = param.Parameter(precedence=-1)


    def __init__(self, layout, keys=None, dimensions=None, create_axes=False, ranges=None,
                 layout_num=1, **params):
        if not keys or not dimensions:
            dimensions, keys = traversal.unique_dimkeys(layout)
        MPLPlot.__init__(self, dimensions=dimensions, keys=keys, **params)
        self.layout = layout
        self.cyclic_index = 0
        self.zorder = 0
        self.layout_num = layout_num
        self.overlaid = False
        self.map = {}
        if layout.ndims > 1:
            xkeys, ykeys = zip(*layout.data.keys())
        else:
            xkeys = layout.keys()
            ykeys = [None]
        self._xkeys = sorted(set(xkeys))
        self._ykeys = sorted(set(ykeys))
        self._xticks, self._yticks = [], []
        self.rows, self.cols = layout.shape
        self.fig_inches = self._get_size()
        _, _, self.layout = self._create_subplots(layout, None, ranges, create_axes=False)
        self.border_extents = self._compute_borders()
        width, height, _, _, _, _ = self.border_extents
        if self.aspect == 'equal':
            self.aspect = float(width/height)

    def get_extents(self, view, ranges):
        width, height, _, _, _, _ = self.border_extents
        return (0, 0, width, height)


    def _get_frame(self, key):
        return GridPlot._get_frame(self, key)


    def initialize_plot(self, ranges=None):
        width, height, b_w, b_h, widths, heights = self.border_extents

        key = self.keys[-1]
        ranges = self.compute_ranges(self.layout, key, ranges)
        self.handles['projs'] = {}
        x, y = b_w, b_h
        for xidx, xkey in enumerate(self._xkeys):
            w = widths[xidx]
            for yidx, ykey in enumerate(self._ykeys):
                h = heights[yidx]
                if self.layout.ndims > 1:
                    vmap = self.layout.get((xkey, ykey), None)
                else:
                    vmap = self.layout.get(xkey, None)
                pane = vmap.select(**{d.name: val for d, val in zip(self.dimensions, key)
                                    if d in vmap.kdims})
                if pane:
                    if issubclass(vmap.type, CompositeOverlay): pane = pane.values()[-1]
                    data = pane.data if pane else None
                else:
                    pane = vmap.last.values()[-1] if issubclass(vmap.type, CompositeOverlay) else vmap.last
                    data = pane.data
                ranges = self.compute_ranges(vmap, key, ranges)
                opts = self.lookup_options(pane, 'style')[self.cyclic_index]
                plot = self.handles['axis'].imshow(data, extent=(x,x+w, y, y+h), **opts)
                valrange = match_spec(pane, ranges)[pane.vdims[0].name]
                plot.set_clim(valrange)
                if data is None:
                    plot.set_visible(False)
                self.handles['projs'][(xkey, ykey)] = plot
                y += h + b_h
                if xidx == 0:
                    self._yticks.append(y-b_h-h/2.)
            y = b_h
            x += w + b_w
            self._xticks.append(x-b_w-w/2.)

        grid_dims = self.layout.kdims
        ydim = grid_dims[1] if self.layout.ndims > 1 else None
        xticks = (self._xticks, self._process_ticklabels(self._xkeys, grid_dims[0]))
        yticks = (self._yticks, self._process_ticklabels(self._ykeys, ydim))
        ylabel = str(self.layout.kdims[1]) if self.layout.ndims > 1 else ''

        return self._finalize_axis(key, ranges=ranges,
                                   title=self._format_title(key),
                                   xticks=xticks, yticks=yticks,
                                   xlabel=str(self.layout.get_dimension(0)),
                                   ylabel=ylabel)


    def update_frame(self, key, ranges=None):
        grid = self._get_frame(key)
        ranges = self.compute_ranges(self.layout, key, ranges)
        for xkey in self._xkeys:
            for ykey in self._ykeys:
                plot = self.handles['projs'][(xkey, ykey)]
                grid_key = (xkey, ykey) if self.layout.ndims > 1 else (xkey,)
                element = grid.data.get(grid_key, None)
                if element:
                    plot.set_visible(True)
                    data = element.values()[0].data if isinstance(element, CompositeOverlay) else element.data
                    plot.set_data(data)
                else:
                    plot.set_visible(False)

        xdim = self.layout.kdims[0]
        ydim = self.layout.kdims[1] if self.layout.ndims > 1 else None

        self._finalize_axis(key, ranges=ranges, title=self._format_title(key),
                            xticks=(self._xticks, self._process_ticklabels(self._xkeys, xdim)),
                            yticks=(self._yticks, self._process_ticklabels(self._ykeys, ydim)))


    def _axis_labels(self, view, subplots, xlabel, ylabel, zlabel):
        xdim = self.layout.kdims[0]
        ydim = self.layout.kdims[1] if self.layout.ndims > 1 else None
        return xlabel if xlabel else str(xdim), ylabel if ylabel or not ydim else str(ydim), zlabel


    def _compute_borders(self):
        ndims = self.layout.ndims
        xkey, ykey = self._xkeys[0], self._ykeys[0]
        width_fn = lambda x: x.range(0)
        height_fn = lambda x: x.range(1)
        if ndims > 1:
            vert_section = self.layout[xkey, slice(None)]
        else:
            vert_section = [self.layout[xkey]]
        horz_section = self.layout[(slice(None), ykey) if ndims > 1 else slice(None)]
        height_extents = [max_range(hm.traverse(height_fn, [Element])) for hm in vert_section]
        width_extents = [max_range(hm.traverse(width_fn, [Element])) for hm in horz_section]
        widths = [extent[0]-extent[1] for extent in width_extents]
        heights = [extent[0]-extent[1] for extent in height_extents]
        width, height = np.sum(widths), np.sum(heights)
        border_width = (width*self.padding)/(len(widths)+1)
        border_height = (height*self.padding)/(len(heights)+1)
        width += width*self.padding
        height += height*self.padding

        return width, height, border_width, border_height, widths, heights


    def __len__(self):
        return max([len(self.keys), 1])
