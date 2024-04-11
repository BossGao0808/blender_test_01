import bpy

# 将游标信息读取出来
my_cursor = bpy.context.scene.cursor.location
print(my_cursor)

for obj in range(10):
    print(obj)
    bpy.ops.mesh.primitive_uv_sphere_add(radius = 1, enter_editmode = False, align = 'WORLD', location = my_cursor)

    selected_obj = bpy.context.object
    selected_obj.name = "ASTRO_0" + str(obj)
    selected_obj.data.name = "ASTRO_0" + str(obj) + "_mesh"
    # 打印对象名称
    print("SelectedObjName:%s" % selected_obj.data.name)

    my_cursor.x += 2
    my_cursor.y += 2
