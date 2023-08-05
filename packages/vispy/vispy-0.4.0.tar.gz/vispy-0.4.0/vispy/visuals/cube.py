# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2015, Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

from ..geometry import create_cube
from ..gloo import set_state
from .mesh import MeshVisual


class CubeVisual(MeshVisual):
    """Visual that displays a cube or cuboid

    Parameters
    ----------
    size : float or tuple
        The size of the cuboid. A float gives a cube, whereas tuples may
        specify the size of each axis (x, y, z) independently.
    vertex_colors : ndarray
        Same as for `MeshVisual` class. See `create_cube` for vertex ordering.
    face_colors : ndarray
        Same as for `MeshVisual` class. See `create_cube` for vertex ordering.
    color : Color
        The `Color` to use when drawing the cube faces.
    edge_color : tuple or Color
        The `Color` to use when drawing the cube edges. If `None`, then no
        cube edges are drawn.
    """
    def __init__(self, size=1.0, vertex_colors=None, face_colors=None,
                 color=(0.5, 0.5, 1, 1), edge_color=None):
        vertices, filled_indices, outline_indices = create_cube()
        vertices['position'] *= size

        MeshVisual.__init__(self, vertices['position'], filled_indices,
                            vertex_colors, face_colors, color)
        if edge_color:
            self._outline = MeshVisual(vertices['position'], outline_indices,
                                       color=edge_color, mode='lines')
        else:
            self._outline = None

    def draw(self, transforms):
        """Draw the visual

        Parameters
        ----------
        transforms : instance of TransformSystem
            The transforms to use.
        """
        MeshVisual.draw(self, transforms)
        if self._outline:
            set_state(polygon_offset=(1, 1), polygon_offset_fill=True)
            self._outline.draw(transforms)
