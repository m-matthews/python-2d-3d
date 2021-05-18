# Pyramid

import bpy
from mathutils import Vector

verts = [
    Vector([-1.0, -1.0, 0.0]),
    Vector([1.0, -1.0, 0.0]),
    Vector([1.0, 1.0, 0.0]),
    Vector([-1.0, 1.0, 0.0]),
    Vector([0.0, 0.0, 1.0])
]
faces = [
    (3, 2, 1, 0),
    (0, 1, 4),
    (1, 2, 4),
    (2, 3, 4),
    (3, 0, 4)
]

mesh = bpy.data.meshes.new("PyramidMesh")
mesh.from_pydata(verts, [], faces)

obj = bpy.data.objects.new("PyramidObject", mesh)
bpy.context.scene.collection.objects.link(obj)

bpy.context.view_layer.objects.active = obj
