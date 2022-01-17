from . helpers.assign_vertex import AssignVertex_01, AssignVertex_02, AssignVertex_03, AssignVertex_04, AssignVertex_05
from . helpers.assign_vertex import AssignVertex_06, AssignVertex_07, AssignVertex_08, AssignVertex_09, AssignVertex_10
from . helpers.assign_vertex import AssignVertex_11, AssignVertex_12, AssignVertex_13, AssignVertex_14, AssignVertex_15
from . helpers.assign_vertex import AssignVertex_16, AssignVertex_17, AssignVertex_18, AssignVertex_19, AssignVertex_20
from . helpers.assign_vertex import AssignVertex_Custom
from . helpers.fix_scale import FixScale
from . helpers.material_to_vertexpaint import MaterialToVertexPaint
from . helpers.material_to_vertexpaint_selected import MaterialToVertexPaintSelected
from . helpers.parent_mesher import Parent_Mesher

from . MaterialPainter.materialPainter_Panel import MaterialPainter_Panel
from . panel import Panel
import bpy

bl_info = {
    "name": "Sean Helpers",
    "author": "Sean Thomas<aurorasean@gmail.com",
    "description": "Sean Helpers",
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
           AssignVertex_Custom, FixScale, MaterialToVertexPaintSelected,
           MaterialPainter_Panel
           )

register, unregister = bpy.utils.register_classes_factory(classes)
