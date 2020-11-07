import bpy

class Panel(bpy.types.Panel):
    bl_idname = "PANEL_PT_PARENT_MESH"
    bl_label = "Parent Mesh Panel"
    bl_category = "Mesh Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context): 
        layout = self.layout

        row = layout.row()
        row.operator('view3d.parent_mesh_armature', text="Create Armature from Parents")

        rowVertex = layout.row()
        rowVertex.operator('view3d.material_to_vertex_paint', text="Material to Vertex paint")