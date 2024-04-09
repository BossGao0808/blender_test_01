import bpy

# 创建一个 cube
bpy.ops.mesh.primitive_cube_add()
cube = bpy.context.object

# 为cube 添加细分修改器
cube.modifiers.new("Test_01", type='SUBSURF')

# 设置细分修改器的视图级别
bpy.context.object.modifiers['Test_01'].levels = 2
# 设置细分修改器的渲染级别
bpy.context.object.modifiers['Test_01'].render_levels = 3
# 设置细分修改器的优化显示
bpy.context.object.modifiers['Test_01'].show_only_control_edges = False
