import bpy
from . panel_custom import panel_custom
from . panel_simple import panel_simple

class Panel(bpy.types.Panel):
    planelCustom = panel_custom()
    bl_idname = "PANEL_PT_PARENT_MESH"
    bl_label = "Parent Mesh Panel"
    bl_category = "Sean Helpers"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def register():
        bpy.types.Scene.mytool_color = bpy.props.FloatVectorProperty(
            name="Color Picker",
            subtype="COLOR",
            size=4,
            min=0.0,
            max=1.0,
                    default=(1.0, 1.0, 1.0, 1.0))

    def draw(self, context):
        panel_simple.draw(self, context)
        self.planelCustom.draw(self, context)
