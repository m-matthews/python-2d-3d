# Triangle

import bpy
from mathutils import Vector

verts = [
    Vector([-1.0, 0.0, 0.0]),
    Vector([1.0, 0.0, 0.0]),
    Vector([0.0, 1.0, 0.0])
]
faces = [(0, 1, 2)]

mesh = bpy.data.meshes.new("TriangleMash")
mesh.from_pydata(verts, [], faces)

obj = bpy.data.objects.new("TriangleObject", mesh)
bpy.context.scene.collection.objects.link(obj)

bpy.context.view_layer.objects.active = obj
