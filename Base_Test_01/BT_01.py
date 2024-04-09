import bpy
from math import radians

#将游标信息读取出来
cursor_Location = bpy.context.scene.cursor.location
print(cursor_Location)

#创建一个cube，并将其位置设置为游标位置
bpy.ops.mesh.primitive_cube_add(size=2, location=cursor_Location)