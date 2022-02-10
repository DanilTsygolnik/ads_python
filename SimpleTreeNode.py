class SimpleTreeNode:

    def __init__(self, val=None, parent=None):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []
        self.NodeLevel = None
        if self.Parent is None:
            self.NodeLevel = 0
        else:
            self.NodeLevel = self.Parent.NodeLevel + 1
