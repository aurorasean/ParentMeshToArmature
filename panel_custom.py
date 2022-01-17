import bpy


class panel_custom:
    array = []

    def __init__(self):
        example1 = {
            "color": {"x": 1, "y": 1, "z": 0},
            "name": "example",
            "icon": "COLLECTION_COLOR_05"
        }
        self.array.append(example1)
        test = bpy.utils.user_resource('CONFIG')
        print(test)

    def draw(self, blenderSelf, context):
        layout = blenderSelf.layout
        rowVertex = layout.row()
        rowVertex.label(text="Text goes here")

        mode = context.object.mode

        enabled = False

        if(mode == "EDIT"):
            enabled = True
        else:
            enabled = False

        for element in self.array:
            row = layout.row()
            row.enabled = enabled
            col = row.column()
            
            col.operator('view3d.assignvertex_16', text='',
                         icon=element["icon"])

            col = row.column()
            col.operator('view3d.fix_scale', text='Fix scale')
