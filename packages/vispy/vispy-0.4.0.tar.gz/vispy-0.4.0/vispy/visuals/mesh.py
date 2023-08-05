# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2015, Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

""" A MeshVisual Visual that uses the new shader Function.
"""

from __future__ import division

import numpy as np

from .visual import Visual
from .shaders import ModularProgram, Function, Varying
from ..gloo import VertexBuffer, IndexBuffer
from ..geometry import MeshData
from ..color import Color

## Snippet templates (defined as string to force user to create fresh Function)
# Consider these stored in a central location in vispy ...


vertex_template = """

void main() {
    gl_Position = $transform($to_vec4($position));
}
"""

fragment_template = """
void main() {
    gl_FragColor = $color;
}
"""

phong_template = """
vec4 phong_shading(vec4 color) {
    vec4 o = $transform(vec4(0, 0, 0, 1));
    vec4 n = $transform(vec4($normal, 1));
    vec3 norm = normalize((n-o).xyz);
    vec3 light = normalize($light_dir.xyz);
    float p = dot(light, norm);
    p = (p < 0. ? 0. : p);
    vec4 diffuse = $light_color * p;
    diffuse.a = 1.0;
    p = dot(reflect(light, norm), vec3(0,0,1));
    if (p < 0.0) {
        p = 0.0;
    }
    vec4 specular = $light_color * 5.0 * pow(p, 100.);
    return color * ($ambient + diffuse) + specular;
}
"""

## Functions that can be used as is (don't have template variables)
# Consider these stored in a central location in vispy ...

vec3to4 = Function("""
vec4 vec3to4(vec3 xyz) {
    return vec4(xyz, 1.0);
}
""")

vec2to4 = Function("""
vec4 vec2to4(vec2 xyz) {
    return vec4(xyz, 0.0, 1.0);
}
""")


class MeshVisual(Visual):
    """Mesh visual

    Parameters
    ----------
    vertices : array-like | None
        The vertices.
    faces : array-like | None
        The faces.
    vertex_colors : array-like | None
        Colors to use for each vertex.
    face_colors : array-like | None
        Colors to use for each face.
    color : instance of Color
        The color to use.
    meshdata : instance of MeshData | None
        The meshdata.
    shading : str | None
        Shading to use.
    mode : str
        The drawing mode.
    **kwargs : dict
        Keyword arguments to pass to `Visual`.
    """
    def __init__(self, vertices=None, faces=None, vertex_colors=None,
                 face_colors=None, color=(0.5, 0.5, 1, 1), meshdata=None,
                 shading=None, mode='triangles', **kwargs):
        Visual.__init__(self, **kwargs)

        self.set_gl_state('translucent', depth_test=True,
                          cull_face=False)

        # Create a program
        self._program = ModularProgram(vertex_template, fragment_template)
        self._program.vert['pre'] = ''
        self._program.vert['post'] = ''
        self._program.frag['pre'] = ''
        self._program.frag['post'] = ''

        # Define buffers
        self._vertices = VertexBuffer(np.zeros((0, 3), dtype=np.float32))
        self._normals = None
        self._faces = IndexBuffer()
        self._colors = VertexBuffer(np.zeros((0, 4), dtype=np.float32))
        self._normals = VertexBuffer(np.zeros((0, 3), dtype=np.float32))

        # Whether to use _faces index
        self._indexed = None

        # Uniform color
        self._color = None

        # primitive mode
        self._mode = mode

        # varyings
        self._color_var = Varying('v_color', dtype='vec4')
        self._normal_var = Varying('v_normal', dtype='vec3')

        # Function for computing phong shading
        self._phong = Function(phong_template)

        # Init
        self.shading = shading
        self._bounds = None
        # Note we do not call subclass set_data -- often the signatures
        # do no match.
        MeshVisual.set_data(self, vertices=vertices, faces=faces,
                            vertex_colors=vertex_colors,
                            face_colors=face_colors, meshdata=meshdata,
                            color=color)

    def set_data(self, vertices=None, faces=None, vertex_colors=None,
                 face_colors=None, color=None, meshdata=None):
        """Set the mesh data

        Parameters
        ----------
        vertices : array-like | None
            The vertices.
        faces : array-like | None
            The faces.
        vertex_colors : array-like | None
            Colors to use for each vertex.
        face_colors : array-like | None
            Colors to use for each face.
        color : instance of Color
            The color to use.
        meshdata : instance of MeshData | None
            The meshdata.
        """
        if meshdata is not None:
            self._meshdata = meshdata
        else:
            self._meshdata = MeshData(vertices=vertices, faces=faces,
                                      vertex_colors=vertex_colors,
                                      face_colors=face_colors)
        self._bounds = self._meshdata.get_bounds()
        if color is not None:
            self._color = Color(color)
        self.mesh_data_changed()

    @property
    def mode(self):
        """The triangle mode used to draw this mesh.

        Options are:

            * 'triangles': Draw one triangle for every three vertices
              (eg, [1,2,3], [4,5,6], [7,8,9)
            * 'triangle_strip': Draw one strip for every vertex excluding the
              first two (eg, [1,2,3], [2,3,4], [3,4,5])
            * 'triangle_fan': Draw each triangle from the first vertex and the
              last two vertices (eg, [1,2,3], [1,3,4], [1,4,5])
        """
        return self._mode

    @mode.setter
    def mode(self, m):
        modes = ['triangles', 'triangle_strip', 'triangle_fan']
        if m not in modes:
            raise ValueError("Mesh mode must be one of %s" % ', '.join(modes))
        self._mode = m

    @property
    def mesh_data(self):
        """The mesh data"""
        return self._meshdata

    @property
    def color(self):
        """The uniform color for this mesh.

        This value is only used if per-vertex or per-face colors are not
        specified.
        """
        return self._color

    @color.setter
    def color(self, c):
        self.set_data(color=c)

    def mesh_data_changed(self):
        self._data_changed = True
        self.update()

    def _update_data(self):
        md = self.mesh_data
        # Update vertex/index buffers
        if self.shading == 'smooth' and not md.has_face_indexed_data():
            v = md.get_vertices()
            if v is None:
                return False
            if v.shape[-1] == 2:
                v = np.concatenate((v, np.zeros((v.shape[:-1] + (1,)))), -1)
            self._vertices.set_data(v, convert=True)
            self._normals.set_data(md.get_vertex_normals(), convert=True)
            self._faces.set_data(md.get_faces(), convert=True)
            self._indexed = True
            if md.has_vertex_color():
                self._colors.set_data(md.get_vertex_colors(), convert=True)
            elif md.has_face_color():
                self._colors.set_data(md.get_face_colors(), convert=True)
            else:
                self._colors.set_data(np.zeros((0, 4), dtype=np.float32))
        else:
            v = md.get_vertices(indexed='faces')
            if v is None:
                return False
            if v.shape[-1] == 2:
                v = np.concatenate((v, np.zeros((v.shape[:-1] + (1,)))), -1)
            self._vertices.set_data(v, convert=True)
            if self.shading == 'smooth':
                normals = md.get_vertex_normals(indexed='faces')
                self._normals.set_data(normals, convert=True)
            elif self.shading == 'flat':
                normals = md.get_face_normals(indexed='faces')
                self._normals.set_data(normals, convert=True)
            else:
                self._normals.set_data(np.zeros((0, 3), dtype=np.float32))
            self._indexed = False
            if md.has_vertex_color():
                self._colors.set_data(md.get_vertex_colors(indexed='faces'),
                                      convert=True)
            elif md.has_face_color():
                self._colors.set_data(md.get_face_colors(indexed='faces'),
                                      convert=True)
            else:
                self._colors.set_data(np.zeros((0, 4), dtype=np.float32))
        self._program.vert['position'] = self._vertices

        # Position input handling
        if v.shape[-1] == 2:
            self._program.vert['to_vec4'] = vec2to4
        elif v.shape[-1] == 3:
            self._program.vert['to_vec4'] = vec3to4
        else:
            raise TypeError("Vertex data must have shape (...,2) or (...,3).")

        # Color input handling
        colors = self._colors if self._colors.size > 0 else self._color.rgba
        self._program.vert[self._color_var] = colors

        # Shading
        if self.shading is None:
            self._program.frag['color'] = self._color_var
        else:
            # Normal data comes via vertex shader
            if self._normals.size > 0:
                normals = self._normals
            else:
                normals = (1., 0., 0.)

            self._program.vert[self._normal_var] = normals
            self._phong['normal'] = self._normal_var

            # Additional phong properties
            self._phong['light_dir'] = (1.0, 1.0, 5.0)
            self._phong['light_color'] = (1.0, 1.0, 1.0, 1.0)
            self._phong['ambient'] = (0.3, 0.3, 0.3, 1.0)

            self._program.frag['color'] = self._phong(self._color_var)

        self._data_changed = False

    @property
    def shading(self):
        """ The shading method used.
        """
        return self._shading

    @shading.setter
    def shading(self, value):
        assert value in (None, 'flat', 'smooth')
        self._shading = value

    def draw(self, transforms):
        """Draw the visual

        Parameters
        ----------
        transforms : instance of TransformSystem
            The transforms to use.
        """
        if self._data_changed:
            if self._update_data() is False:
                return
            self._data_changed = False

        Visual.draw(self, transforms)

        full_tr = transforms.get_full_transform()
        self._program.vert['transform'] = full_tr
        doc_tr = transforms.visual_to_document
        self._phong['transform'] = doc_tr

        # Draw
        if self._indexed:
            self._program.draw(self._mode, self._faces)
        else:
            self._program.draw(self._mode)

    def bounds(self, mode, axis):
        """Get the bounds

        Parameters
        ----------
        mode : str
            Describes the type of boundary requested. Can be "visual", "data",
            or "mouse".
        axis : 0, 1, 2
            The axis along which to measure the bounding values, in
            x-y-z order.
        """
        if self._bounds is None:
            return None
        return self._bounds[axis]
