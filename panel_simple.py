class panel_simple:
    def draw(self, context):
        layout = self.layout

        enabled = False
        if(context.object != None):
            mode = context.object.mode
            if(mode == "EDIT"):
                enabled = True
            else:
                enabled = False

        row = layout.row()

        row = layout.row()
        row.operator('view3d.parent_mesh_armature',
                     text="Create Armature from Parents")

        rowVertex = layout.row()
        rowVertex.label(text="Material to Vertex colour")
        rowVertex = layout.row()

        box = rowVertex.box()
        rowVertex = box.row()
        rowVertex.operator('view3d.material_to_vertex_paint', icon="FREEZE",
                           text="All objects")

        rowVertex = box.row()
        rowVertex.operator('view3d.material_to_vertex_paint_select', icon="DOT",
                           text="Selected objects")
        row = layout.row()

        row = layout.row()
        row.enabled = enabled
        row.label(text="Assign vertex colour")
        row = layout.row()
        box = row.box()
        row = box.row()
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_01', text='', icon='COLORSET_01_VEC')
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_02', text='', icon='COLORSET_02_VEC')
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_03', text='', icon='COLORSET_03_VEC')
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_04', text='', icon='COLORSET_04_VEC')
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_05', text='', icon='COLORSET_05_VEC')

        row = box.row()
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_06', text='', icon='COLORSET_06_VEC')
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_07', text='', icon='COLORSET_07_VEC')
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_08', text='', icon='COLORSET_08_VEC')
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_09', text='', icon='COLORSET_09_VEC')
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_10', text='', icon='COLORSET_10_VEC')

        row = box.row()
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_11', text='', icon='COLORSET_11_VEC')
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_12', text='', icon='COLORSET_12_VEC')
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_13', text='', icon='COLORSET_13_VEC')
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_14', text='', icon='COLORSET_14_VEC')
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_15', text='', icon='COLORSET_15_VEC')

        # these are blank
        row = box.row()
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_16', text='',
                     icon='COLLECTION_COLOR_01')
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_17', text='',
                     icon='COLLECTION_COLOR_02')
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_18', text='',
                     icon='COLLECTION_COLOR_03')
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_19', text='',
                     icon='COLLECTION_COLOR_04')
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_20', text='',
                     icon='COLLECTION_COLOR_05')

        row = layout.row()
        row.enabled = enabled
        row.prop(context.scene, "mytool_color")
        col = row.column()
        col.enabled = enabled
        col.operator('view3d.assignvertex_custom', text='Assign',
                     icon='COLLECTION_COLOR_01')

        row = layout.row()
        row.label(text="Helpers")

        col = row.column()
        col.operator('view3d.fix_scale', text='Fix scale')
