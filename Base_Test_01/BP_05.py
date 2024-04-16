import bpy

# 创建一个平面
bpy.ops.mesh.primitive_plane_add(size = 15, enter_editmode = False, align = 'WORLD', location = (0, 0, 0),
                                 scale = (1, 1, 1))

for obj in bpy.context.selected_objects:
    obj.name = "Plane_01"
    obj.data.name = "Plane_01_mesh"

# 设置为编辑模式
bpy.ops.object.mode_set(mode = 'EDIT')

# 细分为4段
bpy.ops.mesh.subdivide(number_cuts = 4)

# 设置为对象模式
bpy.ops.object.mode_set(mode = 'OBJECT')

vertexlist = [2, 19, 18, 17, 16, 3]

# 将指定的顶点向上移动6个单位
for num in vertexlist:
    bpy.data.objects['Plane_01'].data.vertices[num].co.z += 6

bpy.ops.object.subdivision_set(level = 4, relative = False)

bpy.context.object.modifiers["Subdivision"].show_only_control_edges = False

# 设置为平滑
bpy.ops.object.shade_smooth()

# 创建一个 相机
bpy.ops.object.camera_add(enter_editmode = False, align = 'VIEW', location = (3.4821, -13.4312, 5.43176),
                          rotation = (1.3, -0.04, 0.22), scale = (1, 1, 1))

# 创建一个猴头
bpy.ops.mesh.primitive_monkey_add(size = 2, enter_editmode = False, align = 'WORLD', location = (0, 0, 2),
                                  scale = (1, 1, 1))
bpy.ops.object.subdivision_set(level = 2, relative = False)
bpy.ops.object.shade_smooth()

# 创建一个面光源，位置在(0, 0, 4)，大小为6，命名为AreaLight
bpy.ops.object.light_add(type = 'AREA', align = 'WORLD', location = (0, 0, 4), scale = (6, 6, 6))
bpy.context.object.data.energy = 20
bpy.context.object.data.name = "AreaLight"
bpy.context.object.scale = (6, 6, 6)
