import bpy

class ColourCreateData():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def returnColour(self):
        return (self.x, self.y, self.z)


class AssignVertex():
    colours = {
        "orange": ColourCreateData(0.8, 0.4, 0),
        "red": ColourCreateData(1, 0, 0),
        "blue": ColourCreateData(0, 0, 1),
        "green": ColourCreateData(0, 1, 0),
        "yellow": ColourCreateData(1, 1, 0),
        "purple": ColourCreateData(0.8, 0, 0.8),
        "cyan": ColourCreateData(0, 1, 1),
        "brown": ColourCreateData(0.4, 0.2, 0),
        "mageneta": ColourCreateData(0.8, 0, 0.4),
        "black": ColourCreateData(0, 0, 0),
        "lgreen": ColourCreateData(0.6, 1, 0.6),
        "lblue": ColourCreateData(0, 0.4, 1),
        "lred": ColourCreateData(0.8, 0, 0),
        "dgreen": ColourCreateData(0, 0.8, 0),
        "lyellow": ColourCreateData(0.4, 0.4, 0),
        "royalblue": ColourCreateData(0.254901960784314, 0.411764705882353, 0.882352941176471),
        "slateblue ": ColourCreateData(0.415686274509804, 0.352941176470588, 0.803921568627451),
        "orchid ": ColourCreateData(0.854901960784314, 0.43921568627451, 0.83921568627451),
        "lavender ": ColourCreateData(0.901960784313726, 0.901960784313726, 0.980392156862745),
        "lightcoral ": ColourCreateData(0.941176470588235, 0.501960784313725, 0.501960784313725),
        "lawngreen ": ColourCreateData(0.486274509803922, 0.988235294117647, 0),
    }

    def AssignVertexColourCustom(self, colour):
        mode = bpy.context.object.mode

        bpy.ops.paint.vertex_paint_toggle()
        bpy.context.object.data.use_paint_mask = True
        bpy.data.brushes["Draw"].color = colour
        bpy.ops.paint.vertex_color_set()
        bpy.ops.paint.vertex_color_set()
        bpy.ops.paint.vertex_paint_toggle()
        bpy.ops.object.mode_set(mode=mode)

    def AssignVertexColour(self, colour):
        mode = bpy.context.object.mode

        selected = self.colours[colour]
        bpy.ops.paint.vertex_paint_toggle()
        bpy.context.object.data.use_paint_mask = True
        bpy.data.brushes["Draw"].color = selected.returnColour()
        bpy.ops.paint.vertex_color_set()
        bpy.ops.paint.vertex_color_set()
        bpy.ops.paint.vertex_paint_toggle()
        bpy.ops.object.mode_set(mode=mode)


class AssignVertex_01(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_01"
    bl_label = "Assign vertex red"

    def execute(self, context):
        self.assign.AssignVertexColour('red')
        return {'FINISHED'}


class AssignVertex_02(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_02"
    bl_label = "Assign vertex orange"

    def execute(self, context):
        self.assign.AssignVertexColour('orange')
        return {'FINISHED'}


class AssignVertex_03(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_03"
    bl_label = "Assign vertex green"

    def execute(self, context):
        self.assign.AssignVertexColour('green')
        return {'FINISHED'}


class AssignVertex_04(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_04"
    bl_label = "Assign vertex blue"

    def execute(self, context):
        self.assign.AssignVertexColour('blue')
        return {'FINISHED'}


class AssignVertex_05(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_05"
    bl_label = "Assign vertex lred"

    def execute(self, context):
        self.assign.AssignVertexColour('lred')
        return {'FINISHED'}


class AssignVertex_06(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_06"
    bl_label = "Assign vertex purple"

    def execute(self, context):
        self.assign.AssignVertexColour('purple')
        return {'FINISHED'}


class AssignVertex_07(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_07"
    bl_label = "Assign vertex 07"

    def execute(self, context):
        self.assign.AssignVertexColour('cyan')
        return {'FINISHED'}


class AssignVertex_08(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_08"
    bl_label = "Assign vertex lblue"

    def execute(self, context):
        self.assign.AssignVertexColour('lblue')
        return {'FINISHED'}


class AssignVertex_09(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_09"
    bl_label = "Assign vertex yellow"

    def execute(self, context):
        self.assign.AssignVertexColour('yellow')
        return {'FINISHED'}


class AssignVertex_10(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_10"
    bl_label = "Assign vertex black"

    def execute(self, context):
        self.assign.AssignVertexColour('black')
        return {'FINISHED'}


# ----------------------------


class AssignVertex_11(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_11"
    bl_label = "Assign vertex mageneta"

    def execute(self, context):
        self.assign.AssignVertexColour('mageneta')
        return {'FINISHED'}


class AssignVertex_12(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_12"
    bl_label = "Assign vertex lgreen"

    def execute(self, context):
        self.assign.AssignVertexColour('lgreen')
        return {'FINISHED'}


class AssignVertex_13(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_13"
    bl_label = "Assign vertex lavender "

    def execute(self, context):
        self.assign.AssignVertexColour('lavender')
        return {'FINISHED'}


class AssignVertex_14(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_14"
    bl_label = "Assign vertex brown"

    def execute(self, context):
        self.assign.AssignVertexColour('brown')
        return {'FINISHED'}


class AssignVertex_15(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_15"
    bl_label = "Assign vertex dgreen"

    def execute(self, context):
        self.assign.AssignVertexColour('dgreen')
        return {'FINISHED'}

# ----------------
class AssignVertex_16(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_16"
    bl_label = "Assign vertex lawngreen "

    def execute(self, context):
        self.assign.AssignVertexColour('lawngreen')
        return {'FINISHED'}


class AssignVertex_17(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_17"
    bl_label = "Assign vertex orchid"
    
    def execute(self, context):
        self.assign.AssignVertexColour('orchid')
        return {'FINISHED'}


class AssignVertex_18(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_18"
    bl_label = "Assign vertex slateblue "

    def execute(self, context):
        self.assign.AssignVertexColour('slateblue')
        return {'FINISHED'}


class AssignVertex_19(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_19"
    bl_label = "Assign vertex lightcoral "

    def execute(self, context):
        self.assign.AssignVertexColour('lightcoral')
        return {'FINISHED'}


class AssignVertex_20(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_20"
    bl_label = "Assign vertex royalblue"

    def execute(self, context):
        self.assign.AssignVertexColour('royalblue')
        return {'FINISHED'}

class AssignVertex_Custom(bpy.types.Operator):
    assign = AssignVertex()
    bl_idname = "view3d.assignvertex_custom"
    bl_label = "Assign vertex custom"
    
    def execute(self, context):
        tempColour = context.scene.mytool_color
        colour = (tempColour[0], tempColour[1], tempColour[2])
        self.assign.AssignVertexColourCustom(colour)
        return {'FINISHED'}

