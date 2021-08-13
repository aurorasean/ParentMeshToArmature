import bpy
from .. scene_helper import SceneHelper


class FixScale(bpy.types.Operator):

    bl_idname = "view3d.fix_scale"
    bl_label = "Fix Scale"

    def execute(self, context):
        selected = SceneHelper.getSelected()
        if(selected != None):
            deltaScale = selected.delta_scale
            if(deltaScale[0] != 1 or deltaScale[1] != 1 or deltaScale[2] != 1):                                
                bpy.ops.object.transform_apply(
                    location=False, rotation=False, scale=True)
                # bpy.ops.object.transforms_to_deltas(mode='SCALE')
                # bpy.ops.transform.resize(value=(deltaScale[0], deltaScale[1], deltaScale[2]), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL',
                #                          mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
                # bpy.ops.object.transform_apply(
                #     location=False, rotation=False, scale=True)
                bpy.context.object.delta_scale[0] = 1
                bpy.context.object.delta_scale[1] = 1
                bpy.context.object.delta_scale[2] = 1

                print('scale fixed %s' % selected.delta_scale)

        return {'FINISHED'}
