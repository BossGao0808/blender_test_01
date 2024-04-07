
import bpy  # 导入 Blender Python API

# 创建一个新的面板类，继承自 bpy.types.Panel
class ObjectSelectPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_select"  # 面板的内部名称
    bl_label = "Select"  # 面板的标签，会显示在用户界面上
    bl_space_type = 'PROPERTIES'  # 面板所在的空间类型

    bl_region_type = 'WINDOW'  # 面板所在的区域类型
    bl_context = "object"  # 面板的上下文
    bl_options = {'DEFAULT_CLOSED'}  # 面板的选项，这里设置为默认关闭

    @classmethod
    def poll(cls, context):  # 定义一个类方法，用于判断面板是否应该在当前上下文中显示
        return (context.object is not None)  # 如果当前上下文中有活动的对象，就显示面板

    def draw_header(self, context):  # 定义一个方法，用于绘制面板的头部
        layout = self.layout  # 获取面板的布局
        layout.label(text="My Select Panel")  # 在头部添加一个标签

    def draw(self, context):  # 定义一个方法，用于绘制面板的内容
        layout = self.layout  # 获取面板的布局

        box = layout.box()  # 在布局中添加一个新的盒子
        box.label(text="Selection Tools")  # 在盒子中添加一个标签
        box.operator("object.select_all").action = 'TOGGLE'  # 在盒子中添加一个操作按钮，点击后会执行 "object.select_all" 操作，并设置操作的动作为 'TOGGLE'
        row = box.row()  # 在盒子中添加一个新的行
        row.operator("object.select_all").action = 'INVERT'  # 在行中添加一个操作按钮，点击后会执行 "object.select_all" 操作，并设置操作的动作为 'INVERT'
        row.operator("object.select_random")  # 在行中添加一个操作按钮，点击后会执行 "object.select_random" 操作

bpy.utils.register_class(ObjectSelectPanel)  # 注册面板类，这样 Blender 才能在用户界面中显示它
