import bpy
from math import cos, pi, sin, sqrt
from mathutils import Vector
from mathutils.geometry import normal


class KochSnowflake:
    name = "Snowflake"

    def __init__(self, scale, iterations, factor=0.8):
        self.midpoints = {}
        self.faces = []
        self.face_materials = []
        self.materials = self.get_materials(iterations)
        offset = scale / sqrt(2)
        self.verts = [Vector([-offset * sin(pi/6), offset * cos(pi/6), 0]),
                      Vector([offset, 0, 0]),
                      Vector([-offset * sin(pi/6), -offset * cos(pi/6), 0]),
                      Vector([0, 0, self.height(scale)])]

        # Add the four faces of the initial tetrahedron.
        factor = 1.0 if factor > 1.0 else factor
        self.face(0, 1, 2, iterations, 0, factor)
        self.face(0, 2, 3, iterations, 0, factor)
        self.face(0, 3, 1, iterations, 0, factor)
        self.face(2, 1, 3, iterations, 0, factor)

        # Add the Mesh to Blender.
        mesh = bpy.data.meshes.new(self.name)
        mesh.from_pydata(self.verts, [], self.faces)

        obj = bpy.data.objects.new(self.name, mesh)
        for material in self.materials:
            obj.data.materials.append(material)
        for i, poly in enumerate(obj.data.polygons):
            poly.material_index = self.face_materials[i]
        bpy.context.scene.collection.objects.link(obj)

        bpy.context.view_layer.objects.active = obj

    def get_materials(self, iterations):
        """Build the list of materials for each iteration."""
        materials = []
        for i in range(iterations):
            name = f"{self.name}_Mat{i}"
            material = bpy.data.materials.get(name)
            if not material:
                material = bpy.data.materials.new(name)
            materials.append(material)
        return materials

    def height(self, scale):
        """Calculate the height (from base place) of a tetrahedron."""
        return scale * sqrt(6.0) / 3.0

    def midpoint(self, v1, v2):
        """Determine the midpoint between 2 vectors."""
        return (v1 + v2) / 2

    def face(self, i1, i2, i3, iteration, plane, factor):
        """Create the face based on vector indices."""
        if iteration < 1:
            # Final iteration so add the face itself.
            self.faces.append([i1, i2, i3])
            self.face_materials.append(plane)
        else:
            # Split the triangular face into four triangles, with the central
            # one becoming another tetrahedron.
            v4 = self.midpoint(self.verts[i1], self.verts[i2])
            i4 = len(self.verts)
            self.verts.append(v4)
            v5 = self.midpoint(self.verts[i2], self.verts[i3])
            i5 = len(self.verts)
            self.verts.append(v5)
            v6 = self.midpoint(self.verts[i3], self.verts[i1])
            i6 = len(self.verts)
            self.verts.append(v6)

            # Include additional recursion on the small faces if required.
            self.face(i1, i4, i6, iteration - 1, plane, factor)
            self.face(i4, i2, i5, iteration - 1, plane, factor)
            self.face(i6, i5, i3, iteration - 1, plane, factor)

            # Find the center of the new triangle.
            center = (v4 + v5 + v6) / 3

            if factor == 1.0:
                length = (v4 - v5).length
            else:
                v4b = center + (v4 - center) * factor
                i4b = len(self.verts)
                self.verts.append(v4b)
                v5b = center + (v5 - center) * factor
                i5b = len(self.verts)
                self.verts.append(v5b)
                v6b = center + (v6 - center) * factor
                i6b = len(self.verts)
                self.verts.append(v6b)
                length = (v4b - v5b).length
                self.faces.append([i4, i5, i5b, i4b])
                self.face_materials.append(plane)
                self.faces.append([i5, i6, i6b, i5b])
                self.face_materials.append(plane)
                self.faces.append([i6, i4, i4b, i6b])
                self.face_materials.append(plane)

            # Calculate the point for the tetrahedron peak.
            i7 = len(self.verts)
            n = normal(self.verts[i4], self.verts[i5], self.verts[i6]) * self.height(length * factor)
            self.verts.append(Vector([center.x+n.x, center.y+n.y, center.z+n.z]))

            # Add the faces of the central tetrahedron.
            if factor == 1.0:
                self.face(i4, i5, i7, iteration - 1, plane + 1, factor)
                self.face(i6, i4, i7, iteration - 1, plane + 1, factor)
                self.face(i5, i6, i7, iteration - 1, plane + 1, factor)
            else:
                self.face(i4b, i5b, i7, iteration - 1, plane + 1, factor)
                self.face(i6b, i4b, i7, iteration - 1, plane + 1, factor)
                self.face(i5b, i6b, i7, iteration - 1, plane + 1, factor)


KochSnowflake(1, 0, 0.85)
