from . assign_vertex import AssignVertex_01, AssignVertex_02, AssignVertex_03, AssignVertex_04, AssignVertex_05
from . assign_vertex import AssignVertex_06, AssignVertex_07, AssignVertex_08, AssignVertex_09, AssignVertex_10
from . assign_vertex import AssignVertex_11, AssignVertex_12, AssignVertex_13, AssignVertex_14, AssignVertex_15
from . assign_vertex import AssignVertex_16, AssignVertex_17, AssignVertex_18, AssignVertex_19, AssignVertex_20
from . assign_vertex import AssignVertex_Custom
from . fix_scale import FixScale
from . material_to_vertexpaint import MaterialToVertexPaint
from . parent_mesher import Parent_Mesher
from . panel import Panel
import bpy

bl_info = {
    "name": "Parent Mesh to Armature",
    "author": "Sean Thomas<aurorasean@gmail.com",
    "description": "Parent mesh tree to Armature with mesh",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "View3D",
    "category": "Object"
}

classes = (Parent_Mesher, Panel, MaterialToVertexPaint,  AssignVertex_01,
           AssignVertex_02, AssignVertex_03, AssignVertex_04, AssignVertex_05,
           AssignVertex_06, AssignVertex_07, AssignVertex_08, AssignVertex_09, AssignVertex_10,
           AssignVertex_11, AssignVertex_12, AssignVertex_13, AssignVertex_14, AssignVertex_15,
           AssignVertex_16, AssignVertex_17, AssignVertex_18, AssignVertex_19, AssignVertex_20,
           AssignVertex_Custom, FixScale
           )
register, unregister = bpy.utils.register_classes_factory(classes)
