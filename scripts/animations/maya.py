import sys
import argparse

parser = argparse.ArgumentParser(description='Visualisation library for '
                                 'folders with VTK files using Mayavi2'
                                 )

parser.add_argument('vtk_folder_path', help='Path to the folder containing '
                    'the VTK files')

parser.add_argument('--fidimag', help='Using this option the script will try '
                    'filter the points with Ms = 0', action='store_true')

parser.add_argument('--glyphs', help='Plot glyphs', action='store_true')
parser.add_argument('--glyph_style', help='Plot glyphs', default='no_coloring')

parser.add_argument('--data_clip', help='To clip the surface data',
                    action='store_true')

parser.add_argument('--sphere', help='Draw a shpere: radius r_x r_y r_z',
                    nargs=4, type=float)

# Parser arguments
args = parser.parse_args()

import os

# First, and before importing any Enthought packages, set the ETS_TOOLKIT
# environment variable to qt4, to tell Traits that we will use Qt.
# os.environ['ETS_TOOLKIT'] = 'qt5'
# print os.getenv("ETS_TOOLKIT")

from mayavi import mlab
import matplotlib
from matplotlib.cm import datad, get_cmap
import numpy as np

from traits.api import HasTraits, Range, Instance, on_trait_change
from traitsui.api import View, Item, Group

from mayavi.core.api import PipelineBase
from mayavi.core.ui.api import MayaviScene, SceneEditor, MlabSceneModel

import glob

from tvtk.api import tvtk
from mayavi.filters.user_defined import UserDefined


# -----------------------------------------------------------------------------

# Define and apply a UserDefined:CellCenters filter
CellCenter = UserDefined(filter=tvtk.CellCenters())

# -----------------------------------------------------------------------------


"""
This script plots a nanodisk in Mayavi2 with a colormap representing
the z-component of the magnetisation. The script must be run with
an argument corresponding to the path of the .vtu file to be plotted
"""

# # Try to simulate the new default colormap from MATLAB: Parula
# # Remove the first two lines (comments)
# # For the third column, remove the extra '\' (read until the sixth character)
# # for this we use 'converters'
# # Finally, do not consider the 0th column
# my_rgb = np.loadtxt('/home/david/scripts/parula.txt', skiprows=2,
#                     converters={3: lambda s: float(s[:6])},
#                     usecols=(1, 2, 3))
#
# parula = matplotlib.colors.ListedColormap(my_rgb, name='parula')
# values = np.linspace(0., 1., len(my_rgb))
# parula = get_cmap(parula)(values.copy())
# parula[:, 0] = [int(x * 255) for x in parula[:, 0]]
# parula[:, 1] = [int(x * 255) for x in parula[:, 1]]
# parula[:, 2] = [int(x * 255) for x in parula[:, 2]]
# parula[:, 3] = [int(x * 255) for x in parula[:, 3]]
#
# parula = zip(parula[:, 0],
#              parula[:, 1],
#              parula[:, 2],
#              parula[:, 3],)
# # print parula

vtk_folder_path = args.vtk_folder_path
if not vtk_folder_path.endswith('/'):
    vtk_folder_path += '/'

# List of vtk files
vtks_list = sorted(glob.glob(vtk_folder_path + '*.vt*'))

# Check http://docs.enthought.com/mayavi/mayavi/auto/example_
#       mlab_interactive_dialog.html#example-mlab-interactive-dialog


class MyModel(HasTraits):
    snapshot = Range(0, len(vtks_list) - 1, 1)

    scene = Instance(MlabSceneModel, ())
    plot = Instance(PipelineBase)

    # When the scene is activated, or when the parameters are changed, we
    # update the plot.
    @on_trait_change('snapshot, scene.activated')
    def update_plot(self):
        if self.plot is None:
            # We must pass a pipeline to self.plot since it is a
            # PipelineBase
            self.plot = self.plot_scene()
        else:
            # If self.plot exists, just update it
            self.plot.timestep = self.snapshot

    # We initiate the pipeline for the mayavi plot here
    def plot_scene(self):
        # Read the first file from the list
        data = self.scene.mlab.pipeline.open(vtks_list[0])

        if args.fidimag:
            # Extract vector norm and filter the points whose norm is
            # zero (we can set an arbitrary low value)
            vnorm = mlab.pipeline.extract_vector_norm(data)

            vtr.pipeline.surface(vecomp, vmax=1, vmin=-1,
                                                colormap='gist_earth'
                                                )
        # surf.module_manager.scalar_lut_manager.lut.table = parula

        if args.glyphs:
            if not args.fidimag:
                glyphs = mlab.pipeline.glyph(vecomp, mode='arrow')

            else:
                cell_centre = mlab.pipeline.user_defined(data, filter=tvtk.CellCenters())

                vc = mlab.pipeline.extract_vector_components(cell_centre)
                vc.component = 'z-component'  # Extract z-component of telf.scene.mlab.pipeline.glyph(vecomp, mode='arrow')
            # glyphs.glyph.scalets()
