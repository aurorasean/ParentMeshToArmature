
import json
import bpy
import os
from bpy.props import StringProperty, IntProperty, CollectionProperty, BoolProperty, FloatVectorProperty
from bpy.types import PropertyGroup, UIList, Operator, Panel, AddonPreferences
from pathlib import Path

home = str(Path.home())
packageName = 'ParentMesh-to-arm'

def write_colours(data):
    path = os.path.join(home, 'appdata', "material-painter.json")
    with open(path, 'w') as f:
        json.dump(data, f)

def read_colours():
    path = os.path.join(home, 'appdata', "material-painter.json")
    if os.path.exists(path):
        with open(path) as f:
            data = json.load(f)
        return data
    else:
        obj = {
            "colours": [{"name": "black", "colour": 'red'}]
        }
        write_colours(obj)
        return obj

class ListItem(PropertyGroup):
    """Group of properties representing an item in the list."""

    name: StringProperty(
        name="Name",
        description="A name for this item",
        default="Untitled")

    colour: FloatVectorProperty(
        name="Color Picker",
        subtype="COLOR",
        size=4,
        min=0.0,
        max=1.0,
        default=(1.0, 1.0, 1.0, 1.0))


class MaterialPainterAddonPreferences(AddonPreferences):
    # this must match the add-on name, use '__package__'
    # when defining this in a submodule of a python package.
    bl_idname = packageName

    colours: CollectionProperty(type=ListItem)

    def draw(self, context):
        layout = self.layout
        layout.label(text="List of colours for material mapping")
        layout.prop(self, "colours")


class MY_UL_List(UIList):
    """Demo UIList."""

    def draw_item(self, context, layout, data, item, icon, active_data,
                  active_propname, index):

        # We could write some code to decide which icon to use here...
        custom_icon = 'OBJECT_DATAMODE'

        # Make sure your code supports all 3 layout types
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=item.name, icon=custom_icon)

        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text='', icon=custom_icon)

    def draw_filter(self, context, layout):
        """UI code for the filtering/sorting/search area."""

        layout.separator()
        col = layout.column(align=True)

    def filter_items(self, context, data, propname):
        """Filter and order items in the list."""

        filtered = []
        ordered = []
        # Invert the filter
        if filtered and self.invert_filter_by_random:
            show_flag = self.bitflag_filter_item & ~self.bitflag_filter_item

            for i, bitflag in enumerate(filtered):
                if bitflag == filter_flag:
                    filtered[i] = self.bitflag_filter_item
                else:
                    filtered[i] &= ~self.bitflag_filter_item

        return filtered, ordered


class LIST_OT_NewItem(Operator):
    """Add a new item to the list."""

    bl_idname = "my_list.new_item"
    bl_label = "Add a new item"

    def execute(self, context):
        context.scene.my_list.add()
        return{'FINISHED'}


class LIST_OT_LoadAll(Operator):
    bl_idname = "my_list.load_list"
    bl_label = "Load from previous"

    def execute(self, context):
        colourObj = read_colours()
        sceneList = context.scene.my_list
        sceneList.clear()
        for c in colourObj['colours']:
            listItem = sceneList.add()
            listItem.name = c['name']
            listItem.colour = (c['colour-x'], c['colour-x'],
                               c['colour-z'], c['colour-t'])
        return{'FINISHED'}


class LIST_OT_SaveAll(Operator):
    bl_idname = "my_list.save_list"
    bl_label = "Save the list"

    def execute(self, context):
        scene = context.scene
        items = []
        for item in scene.my_list:
            print("item print out: %s" % item.name)
            items.append({
                "name": item.name,
                "colour-x": item.colour[0],
                "colour-y": item.colour[1],
                "colour-z": item.colour[2],
                "colour-t": item.colour[3],
            })
        obj = {
            "colours": items
        }
        write_colours(obj)
        return{'FINISHED'}


class LIST_OT_DeleteItem(Operator):
    """Delete the selected item from the list."""

    bl_idname = "my_list.delete_item"
    bl_label = "Deletes an item"

    @classmethod
    def poll(cls, context):
        return context.scene.my_list

    def execute(self, context):
        my_list = context.scene.my_list
        index = context.scene.list_index

        my_list.remove(index)
        context.scene.list_index = min(max(0, index - 1), len(my_list) - 1)

        return{'FINISHED'}


class MaterialPainter_Panel(bpy.types.Panel):
    bl_idname = "PANEL_PT_PARENT_MESH_MAGIC"
    bl_label = "Material Painter"
    bl_category = "Material Painter"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    loadedPref = False

    def __init__(self) -> None:
        super().__init__()

    def execute(self, context):
        print('hello exec')
        return {'FINISHED'}

    def register():
        print('hello world')
        bpy.utils.register_class(ListItem)
        bpy.types.Scene.my_list = CollectionProperty(type=ListItem)
        bpy.types.Scene.list_index = IntProperty(name="Index for my_list",
                                                 default=0)
        bpy.utils.register_class(MY_UL_List)
        bpy.utils.register_class(LIST_OT_NewItem)
        bpy.utils.register_class(LIST_OT_DeleteItem)
        bpy.utils.register_class(LIST_OT_SaveAll)
        bpy.utils.register_class(MaterialPainterAddonPreferences)
        bpy.utils.register_class(LIST_OT_LoadAll)

    def unregister():
        bpy.utils.unregister_class(ListItem)
        bpy.utils.unregister_class(MY_UL_List)
        del bpy.types.Scene.my_list
        del bpy.types.Scene.list_index
        bpy.utils.unregister_class(LIST_OT_NewItem)
        bpy.utils.unregister_class(LIST_OT_DeleteItem)
        bpy.utils.unregister_class(LIST_OT_SaveAll)
        bpy.utils.unregister_class(MaterialPainterAddonPreferences)
        bpy.utils.unregister_class(LIST_OT_LoadAll)

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        row = layout.row()
        row.template_list("MY_UL_List", "The_List", scene,
                          "my_list", scene, "list_index")
        row = layout.row()
        row.operator('my_list.new_item', text='NEW')
        row.operator('my_list.delete_item', text='REMOVE')
        row = layout.row()
        row.operator('my_list.save_list', text='Save', icon="FILE_TICK")
        row.operator('my_list.load_list', text='Load', icon="FILEBROWSER")

        if scene.list_index >= 0 and scene.my_list:
            item = scene.my_list[scene.list_index]
            layout.row().prop(item, 'name')
            layout.row().prop(item, 'colour')

    if __name__ == "__main__":
        register()
