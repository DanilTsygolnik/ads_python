class SimpleTree:

    def __init__(self, root=None):
        self.Root = root


    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild) # Parent--Child
        NewChild.Parent = ParentNode # Child--Parent


    def DeleteNode(self, NodeToDelete):
        pass


    def GetAllNodes(self):
        pass


    def FindNodesByValue(self, val):
        pass


    def MoveNode(self, OriginalNode, NewParent):
        pass


    def Count(self):
        pass


    def LeafCount(self):
        pass
