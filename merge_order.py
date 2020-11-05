
class DataHold():
    name = None
    isMesh = False
    boneName = None
    boneNameLink = None

    def __init__(self, name, isMesh, boneName):
        self.name = name
        self.isMesh = isMesh
        self.boneName = boneName

    def toString(self):
        return 'Name: |%s| IsMesh: |%s| boneName: |%s| boneNameLink: |%s|' % (self.name, self.isMesh, self.boneName, self.boneNameLink)
class MergeOrder():
    boneNames = []

    def __init__(self, parent: DataHold, child: DataHold, index, rootLevel):
        self.parent = parent
        self.child = child
        self.index = index
        self.rootLevel = rootLevel

    def get_index(self):
        return '%s-%s' % (self.rootLevel, self.index)

    def toBoneNameString(self):
        return 'Target: |%s| Joiner: |%s| Bones: %s' % (self.target, self.joiner, self.boneNames)

    def toString(self):
        return 'index: |%s| Root: |%s| Parent: |%s| Child: |%s|' % (self.index, self.rootLevel, self.parent.toString(), self.child.toString())


