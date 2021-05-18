import bpy
from bpy.props import (
        FloatProperty,
        IntProperty,
        BoolProperty,
        StringProperty,
        )
from bpy.types import Operator
from bpy_extras import object_utils
from math import cos, pi, sin, sqrt
from mathutils import Vector
from mathutils.geometry import normal


NAME = "Snowflake"


def create_mesh_object(context, self, verts, edges, faces, name):
    # Create new mesh
    mesh = bpy.data.meshes.new(name)

    # Make a mesh from a list of verts/edges/faces.
    mesh.from_pydata(verts, edges, faces)

    # Update mesh geometry after adding pydata.
    mesh.update()

    return object_utils.object_data_add(context, mesh, operator=self)


class Snowflake:
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
        self.face(0, 1, 2, iterations, 0, factor)
        self.face(0, 2, 3, iterations, 0, factor)
        self.face(0, 3, 1, iterations, 0, factor)
        self.face(2, 1, 3, iterations, 0, factor)

    def get_materials(self, iterations):
        """Build the list of materials for each iteration."""
        materials = []
        for i in range(iterations+1):
            name = f"{NAME}_Mat{i}"
            material = bpy.data.materials.get(name)
            if not material:
                material = bpy.data.materials.new(name)
            materials.append(material)
        return materials

    def height(self, scale):
        """Calculate the height (from base place) of a tetrahedron."""
        return scale * sqrt(6.0) / 3.0

    def insert_vertex(self, i1, i2, inew):
        """Find any face that has i1, i2 and insert inew between them."""
        for face in self.faces:
            if i1 in face and i2 in face:
                p1 = face.index(i1)
                p2 = face.index(i2)
                if abs(p1-p2) == 1:
                    face.insert(min(p1, p2)+1, inew)

    def midpoint(self, i1, i2):
        """Determine the midpoint between 2 vectors."""
        if (i1, i2) in self.midpoints:
            return self.midpoints[(i1, i2)]
        elif (i2, i1) in self.midpoints:
            return self.midpoints[(i2, i1)]
        else:
            v = (self.verts[i1] + self.verts[i2]) / 2
            i = len(self.verts)
            self.verts.append(v)
            self.midpoints[(i1, i2)] = (i, v)
            self.insert_vertex(i1, i2, i)
            return (i, v)

    def face(self, i1, i2, i3, iteration, plane, factor):
        """Create the face based on vector indices."""
        if iteration < 1:
            # Final iteration so add the face itself.
            self.faces.append([i1, i2, i3])
            self.face_materials.append(plane)
        else:
            # Split the triangular face into four triangles, with the central
            # one becoming another tetrahedron.
            i4, v4 = self.midpoint(i1, i2)
            i5, v5 = self.midpoint(i2, i3)
            i6, v6 = self.midpoint(i3, i1)

            # Find the center of the new triangle.
            center = (v4 + v5 + v6) / 3

            # Create the inset by the supplied factor.
            v4b = center + (v4 - center) * factor
            i4b = len(self.verts)
            self.verts.append(v4b)
            v5b = center + (v5 - center) * factor
            i5b = len(self.verts)
            self.verts.append(v5b)
            v6b = center + (v6 - center) * factor
            i6b = len(self.verts)
            self.verts.append(v6b)
            edge_length = (v4b - v5b).length

            # Add quads around the central tetrahedron.
            self.faces.append([i4, i5, i5b, i4b])
            self.face_materials.append(plane)
            self.faces.append([i5, i6, i6b, i5b])
            self.face_materials.append(plane)
            self.faces.append([i6, i4, i4b, i6b])
            self.face_materials.append(plane)

            # Calculate the point for the tetrahedron peak.
            i7 = len(self.verts)
            n = normal(v4, v5, v6) * self.height(edge_length * factor)
            self.verts.append(Vector([center.x+n.x, center.y+n.y, center.z+n.z]))

            # Add the faces for the surrounding three triangles.
            self.face(i1, i4, i6, iteration - 1, plane, factor)
            self.face(i4, i2, i5, iteration - 1, plane, factor)
            self.face(i6, i5, i3, iteration - 1, plane, factor)

            # Add the faces of the central tetrahedron.
            self.face(i4b, i5b, i7, iteration - 1, plane + 1, factor)
            self.face(i6b, i4b, i7, iteration - 1, plane + 1, factor)
            self.face(i5b, i6b, i7, iteration - 1, plane + 1, factor)


class AddSnowflake(Operator, object_utils.AddObjectHelper):
    bl_idname = "mesh.primitive_snowflake_add"
    bl_label = NAME
    bl_description = "Construct a snowflake mesh"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}

    Snowflake: BoolProperty(name=NAME, default=True, description=NAME)

    name: StringProperty(name="Name", description="Name")

    change: BoolProperty(name="Change", default=False, description="Change Snowflake")

    size: FloatProperty(
        name="Size",
        description="Snowflake size",
        min=0.1,
        max=9999.0,
        default=5.0
    )
    iterations: IntProperty(
        name="Iterations",
        description="Number of iterations for the showflake",
        min=0,
        max=6,
        default=1
    )
    factor: FloatProperty(
        name="Reduction Factor",
        description="Reduction Factor for each iteration of the Snowflake",
        min=0.1,
        max=0.95,
        default=0.9
    )

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        box.prop(self, "size")
        box.prop(self, "iterations")
        box.prop(self, "factor")

        if not self.change:
            # generic transform props
            box = layout.box()
            box.prop(self, 'align', expand=True)
            box.prop(self, 'location', expand=True)
            box.prop(self, 'rotation', expand=True)

    def execute(self, context):
        # turn off 'Enter Edit Mode'
        use_enter_edit_mode = bpy.context.preferences.edit.use_enter_edit_mode
        bpy.context.preferences.edit.use_enter_edit_mode = False

        if bpy.context.mode == 'OBJECT':
            if context.selected_objects != [] and context.active_object and \
               (NAME in context.active_object.data.keys()) and self.change:
                obj = context.active_object
                oldmesh = obj.data
                oldmeshname = obj.data.name

                sf = Snowflake(self.size, self.iterations, self.factor)
                mesh = bpy.data.meshes.new('TMP')
                mesh.from_pydata(sf.verts, [], sf.faces)
                mesh.update()
                obj.data = mesh
                for material in sf.materials:
                    obj.data.materials.append(material)
                for i, poly in enumerate(obj.data.polygons):
                    poly.material_index = sf.face_materials[i]

                bpy.data.meshes.remove(oldmesh)
                obj.data.name = oldmeshname
            else:
                sf = Snowflake(self.size, self.iterations, self.factor)

                obj = create_mesh_object(context, self, sf.verts, [], sf.faces, NAME)
                for material in sf.materials:
                    obj.data.materials.append(material)
                for i, poly in enumerate(obj.data.polygons):
                    poly.material_index = sf.face_materials[i]

            obj.data[NAME] = True
            obj.data['change'] = False
            for prm in SnowflakeParameters():
                obj.data[prm] = getattr(self, prm)

        if bpy.context.mode == 'EDIT_MESH':
            active_object = context.active_object
            name_active_object = active_object.name
            bpy.ops.object.mode_set(mode='OBJECT')
            sf = Snowflake(self.size, self.iterations, self.factor)

            obj = create_mesh_object(context, self, sf.verts, [], sf.faces, 'TMP')
            for material in sf.materials:
                obj.data.materials.append(material)
            for i, poly in enumerate(obj.data.polygons):
                poly.material_index = sf.face_materials[i]

            obj.select_set(True)
            active_object.select_set(True)
            bpy.ops.object.join()
            context.active_object.name = name_active_object
            bpy.ops.object.mode_set(mode='EDIT')

        if use_enter_edit_mode:
            bpy.ops.object.mode_set(mode='EDIT')

        # restore pre operator state
        bpy.context.preferences.edit.use_enter_edit_mode = use_enter_edit_mode

        return {'FINISHED'}


def SnowflakeParameters():
    SnowflakeParameters = [
        "iterations",
        "factor",
        ]
    return SnowflakeParameters


def menu_func(self, context):
    self.layout.operator("mesh.primitive_snowflake_add", icon="FREEZE")


def register():
    # Register the class for the menu.
    bpy.utils.register_class(AddSnowflake)
    bpy.types.VIEW3D_MT_mesh_add.prepend(menu_func)


def unregister():
    # Remove the registered class from the menu.
    bpy.utils.unregister_module(AddSnowflake)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)


if __name__ == "__main__":
    register()
