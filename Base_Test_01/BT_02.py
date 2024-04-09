import bpy
from math import radians

x_rotation = radians(45)
y_rotation = radians(90)
z_rotation = radians(0)

print(x_rotation)


# 创建一个 cube, 并将其旋转 45 度
bpy.ops.mesh.primitive_cube_add()
cube = bpy.context.object
cube.rotation_euler = (x_rotation, y_rotation, z_rotation)
