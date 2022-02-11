class SimpleTree:

    def __init__(self, root=None):
        self.Root = root


    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild) # Parent--Child
        NewChild.Parent = ParentNode # Child--Parent


    def DeleteNode(self, NodeToDelete):
        assert NodeToDelete is not self.Root
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def GetAllNodes(self):
        
        def get_nodes_list(node, product:list):
            result = product + [node]
            if node.Children != []:
                for child in node.Children:
                    result = get_nodes_list(child, result)
            return result

        return get_nodes_list(self.Root, [])


    def FindNodesByValue(self, val):
        pass


    def MoveNode(self, OriginalNode, NewParent):
        pass


    def Count(self):
        pass


    def LeafCount(self):
        pass
