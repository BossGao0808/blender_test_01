import bpy

object_name = "ASTRO_01"  # 请替换为您的对象名称

# 获取对象
mesh_obj = bpy.data.objects[object_name]

print(mesh_obj)

#mesh_obj = bpy.context.object.data

# 设置第 0 个顶点
mesh_obj.data.vertices[0].co = (1.0, 2.0, 3.0)
# 更新 mesh 数据
mesh_obj.data.update()