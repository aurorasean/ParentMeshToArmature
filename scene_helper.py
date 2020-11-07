import bpy
import bmesh
class SceneHelper ():
    
    def unselectAll():
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        for obj in bpy.data.objects:
            obj.select_set(False)
    def getSelected():
        for select in bpy.context.selected_objects:
            return select

    def selectObject(objName):
        obj = bpy.data.objects[objName]
        obj.select_set(True)
        return obj

    def getObject(objName):
        obj = bpy.data.objects[objName]
        return obj
        
    def setActiveObject(obj):
        bpy.context.view_layer.objects.active = obj

    def setEditModeToFace(name):
        obj = SceneHelper.selectObject(name)
        SceneHelper.setActiveObject(obj)
        mesh = bmesh.from_edit_mesh(obj.data)
        mesh.select_mode = {'VERT', 'EDGE', 'FACE'}
        mesh.select_flush_mode()
        bpy.context.tool_settings.mesh_select_mode = (False, False, True)        