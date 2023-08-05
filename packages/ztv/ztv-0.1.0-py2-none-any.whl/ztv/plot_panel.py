from __future__ import absolute_import
import wx
from wx.lib.pubsub import Publisher
from wx.lib.pubsub.core.datamsg import Message
import matplotlib
matplotlib.interactive(True)
matplotlib.use('WXAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.patches import PathPatch
from matplotlib.path import Path
import numpy as np
import sys


class PlotPlotPanel(wx.Panel):
    def __init__(self, parent, dpi=None, **kwargs):
        wx.Panel.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, **kwargs)
        self.ztv_frame = self.GetTopLevelParent()
        self.figure = Figure(dpi=None, figsize=(1.,1.))
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvasWxAgg(self, -1, self.figure)
        self.Bind(wx.EVT_SIZE, self._onSize)

    def _onSize(self, event):
        self._SetSize()

    def _SetSize(self):
        pixels = tuple(self.GetClientSize())
        self.SetSize(pixels)
        self.canvas.SetSize(pixels)
        self.figure.set_size_inches(float(pixels[0])/self.figure.get_dpi(), float(pixels[1])/self.figure.get_dpi())



class PlotPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.ztv_frame = self.GetTopLevelParent()
        self.primary_image_patch = None

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.plot_panel = PlotPlotPanel(self)
        self.sizer.Add(self.plot_panel, 1, wx.LEFT | wx.TOP | wx.EXPAND)
        
        self.hideshow_button = wx.Button(self, wx.ID_ANY, u"Hide", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sizer.Add(self.hideshow_button, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 2)
        self.hideshow_button.Bind(wx.EVT_BUTTON, self.on_hideshow_button)

        self.SetSizer(self.sizer)
        self.Fit()
        self.start_pt = wx.RealPoint(0., 0.)
        self.end_pt = wx.RealPoint(0., 0.)
        self.redraw()
        Publisher().subscribe(self.on_new_xy0, "new_slice_plot_xy0")
        Publisher().subscribe(self.on_new_xy1, "new_slice_plot_xy1")
        Publisher().subscribe(self.redraw, "primary_xy_limits-changed")
        Publisher().subscribe(self.redraw, "redraw_image")

    def on_new_xy0(self, msg):
        if isinstance(msg, Message):
            x,y = msg.data
        else:
            x,y = msg
        self.start_pt.x, self.start_pt.y = x, y
        self.redraw_overplot_on_image()
        self.redraw()

    def on_new_xy1(self, msg):   
        if isinstance(msg, Message):
            x,y = msg.data
        else:
            x,y = msg
        self.end_pt.x, self.end_pt.y = x, y
        self.redraw_overplot_on_image()
        self.redraw()

    def redraw_overplot_on_image(self):
        if self.primary_image_patch is not None:
            self.ztv_frame.primary_image_panel.axes.patches.remove(self.primary_image_patch)
        path = Path([self.start_pt, self.end_pt], [Path.MOVETO, Path.LINETO])
        self.primary_image_patch = PathPatch(path, color='orange', lw=1)
        self.ztv_frame.primary_image_panel.axes.add_patch(self.primary_image_patch)
        self.ztv_frame.primary_image_panel.figure.canvas.draw()
        self.hideshow_button.SetLabel(u"Hide")        

    def remove_overplot_on_image(self):
        if self.primary_image_patch is not None:
            self.ztv_frame.primary_image_panel.axes.patches.remove(self.primary_image_patch)
        self.ztv_frame.primary_image_panel.figure.canvas.draw()
        self.primary_image_patch = None
        self.hideshow_button.SetLabel(u"Show")

    def on_hideshow_button(self, event):
        if self.hideshow_button.GetLabel() == 'Hide':
            self.hideshow_button.SetLabel(u"Show")
            self.remove_overplot_on_image()
        else:
            self.hideshow_button.SetLabel(u"Hide")        
            self.redraw_overplot_on_image()
            
    def redraw(self, *args):
        xy_limits = self.ztv_frame.primary_image_panel.set_and_get_xy_limits()
        oversample_factor = 10.
        n_pts = oversample_factor*np.max(self.ztv_frame.display_image.shape)
        xs = np.linspace(self.start_pt.x, self.end_pt.x, n_pts)
        ys = np.linspace(self.start_pt.y, self.end_pt.y, n_pts)
        mask = ((xs >= min(xy_limits['xlim'])) & (xs <= max(xy_limits['xlim'])) & 
                (ys >= min(xy_limits['ylim'])) & (ys <= max(xy_limits['ylim'])))
        xs = xs[mask]
        ys = ys[mask]
        if len(xs) > 0:
            if (ys.max() - ys.min()) > (xs.max() - xs.min()):   # dominantly a vertical slice
                if ys[0] > ys[1]:
                    xs = xs[-1::-1]
                    ys = ys[-1::-1]
            else:
                if xs[0] > xs[1]:
                    xs = xs[-1::-1]
                    ys = ys[-1::-1]
            if np.min(np.round(xs)) == np.max(np.round(xs)):
                positions = ys
            elif np.min(np.round(ys)) == np.max(np.round(ys)):
                positions = xs
            else:
                positions = np.sqrt( (xs - xs[0])**2 + (ys - ys[0])**2 )
            xs = xs.astype(np.int)
            ys = ys.astype(np.int)
            im_values = self.ztv_frame.display_image[ys, xs]
            self.plot_panel.axes.clear()
            if positions.min() != positions.max():
                self.line_plot = self.plot_panel.axes.plot(positions, im_values)
                self.plot_panel.axes.set_xlim([positions[0], positions[-1]])
            self.plot_panel.figure.canvas.draw()
        else:
            self.plot_panel.axes.clear()
            self.plot_panel.figure.canvas.draw()
        