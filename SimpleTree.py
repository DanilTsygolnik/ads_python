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
        
        def get_nodes_list(node, product:list, val):
            result = product
            if node.NodeValue == val:
                result.append(node)
            if node.Children != []:
                for child in node.Children:
                    result = get_nodes_list(child, result, val)
            return result

        return get_nodes_list(self.Root, [], val)


    def MoveNode(self, OriginalNode, NewParent):
        if OriginalNode is self.Root:
            raise ValueError('Root can not be moved. Please, choose another node.')
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)


    def Count(self):
        pass


    def LeafCount(self):
        pass
