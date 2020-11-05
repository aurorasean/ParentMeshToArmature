import bpy
class SceneHelper ():
    
    def unselectAll():
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
