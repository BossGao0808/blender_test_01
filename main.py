import bpy

# 创建一个 cube
bpy.ops.mesh.primitive_cube_add()

# 获取 cube 对象
cube = bpy.context.object

# 设置 cube 的名称
cube.name = "ASTRO_01"

# 设置 cube 的位置
cube.location = (0, 0, 0)


#cube = bpy.data.objects['ASTRO_01']

# 获取 cube 的 mesh 数据
mesh = cube.data

# 获取第 0 个顶点
vert = mesh.vertices[0]

# 设置第 0 个顶点的坐标
vert.co = (1.0, 2.0, 3.0)

# 更新 mesh 数据
mesh.update()
#cube.data.vertices[0].co = (1.0, 2.0, 3.0)

#cube.data.update()
