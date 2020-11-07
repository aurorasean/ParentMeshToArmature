import bpy
import bmesh
import random

from . merge_order import MergeOrder, DataHold
from . bone_helper import BoneHelper
from . scene_helper import SceneHelper


class ColourCreateData():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class MaterialToVertexPaint(bpy.types.Operator):
    bl_idname = "view3d.material_to_vertex_paint"
    bl_label = "Material to Vertex paint"
    bl_description = "Material to Vertex paint"
    index = 0
    bone_prefix = "bn_"
    root_prefix = "rt_"
    allowedTypes = ['MESH']
    meshTypes = ['MESH']
    colours = [
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 1),
        (1, 1, 1),
        (1, 1, 0),
        (1, 0, 0),
        (0, 1, 0),
        (1, 0, 1),
    ]

    def createColours(self, max = 100):
        listStart = []
        listStart.append(ColourCreateData(1, 0, 1))
        listStart.append(ColourCreateData(0, 0, 1))
        listStart.append(ColourCreateData(1, 0, 0))
        listStart.append(ColourCreateData(0, 1, 1))
        listStart.append(ColourCreateData(0, 1, 0))
        listStart.append(ColourCreateData(1, 1, 0))
        listStart.append(ColourCreateData(1, 0, 0))
        listStart.append(ColourCreateData(0, 0, 1))

        for ls in listStart:
            for rng in range(max):
                rX = ls.x
                rY = ls.y
                rZ = ls.z
                if rX == 1:
                    rX = random.randrange(0, 99) / 100
                if rY == 1:
                    rY = random.randrange(0, 99) / 100
                if rZ == 1:
                    rZ = random.randrange(0, 99) / 100
                
                newColour = (rX, rY, rZ)
                while newColour in self.colours:
                    rX = random.randrange(0, 99) / 100
                    rY = random.randrange(0, 99) / 100
                    rZ = random.randrange(0, 99) / 100
                    newColour = (rX, rY, rZ)
                self.colours.append(newColour)

        print(self.colours)

    def getDictChildren(self):
        data = []
        for obj in bpy.data.objects:
            if obj.visible_get() and str(obj.type) in self.allowedTypes:
                data.append(obj)
        return data

    def getColour(self):
        maxColour = len(self.colours)
        randomIndex = random.randrange(0, maxColour - 1)
        colour = self.colours[randomIndex]
        self.colours.remove(colour)
        return colour

    def execute(self, context):
        SceneHelper.unselectAll()
        self.createColours() # About 807 colours to choose from
        print('------------------------------------------------------------------------------------------------')
        for obj in self.getDictChildren():
            SceneHelper.unselectAll()
            SceneHelper.selectObject(obj.name)
            SceneHelper.setActiveObject(obj)
            bpy.ops.object.mode_set(mode='EDIT')

            obj = bpy.context.active_object

            materialPolys = {ms.material.name: [] for ms in obj.material_slots}
            for i, p in enumerate(obj.data.polygons):
                materialPolys[obj.material_slots[p.material_index].name].append(
                    i)
            

            for i, p in enumerate(materialPolys):         
                bpy.ops.object.mode_set(mode='EDIT')       
                mesh = bmesh.from_edit_mesh(obj.data)
                SceneHelper.setEditModeToFace(obj.name)

                for face in mesh.faces:
                    face.select = False
                for faceId in materialPolys[p]:
                    for face in mesh.faces:
                        if(face.index == faceId):
                            face.select = True
                
                vertColour = self.getColour()
                bpy.ops.paint.vertex_paint_toggle()
                bpy.context.object.data.use_paint_mask = True
                bpy.data.brushes["Draw"].color = vertColour
                bpy.ops.paint.vertex_color_set()
                bpy.ops.paint.vertex_color_set()
                bpy.ops.paint.vertex_paint_toggle()                
            bpy.ops.object.mode_set(mode='OBJECT')
            SceneHelper.unselectAll()

        print('------------------------------------------------------------------------------------------------')
        print('Finished')
        return {'FINISHED'}
