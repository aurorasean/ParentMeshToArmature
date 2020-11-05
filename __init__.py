
import bpy

bl_info = {
    "name" : "Parent Mesh to Armature",
    "author" : "Sean Thomas<aurorasean@gmail.com",
    "description" : "Parent mesh tree to Armature with mesh",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "category" : "Object"
}

from . panel import Panel
from . parent_mesher import Parent_Mesher

classes = (Parent_Mesher, Panel)
register, unregister = bpy.utils.register_classes_factory(classes)