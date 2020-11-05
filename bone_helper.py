
class BoneHelper():

    def poseBoneSelect(bone, state):
        bone.select = state

    def boneSelect(bone, state):
        bone.select_tail = state
        bone.select_head = state
        bone.select = state

    def doesBoneExist(edit_bones, boneName):
        for bone in edit_bones:
            if bone.name == boneName:
                return True
        return False
