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

        if self.Root is None:
            return []
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

        if self.Root is None:
            return []
        return get_nodes_list(self.Root, [], val)


    def MoveNode(self, OriginalNode, NewParent):
        if OriginalNode is self.Root:
            raise ValueError('Root can not be moved. Please, choose another node.')
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)


    def Count(self):
        return len(self.GetAllNodes())


    def LeafCount(self):

        def count_leaves(node, leaves_num):
            if node.Children == []:
                return leaves_num + 1
            result = leaves_num
            for child in node.Children:
                result = count_leaves(child, result)
            return result

        if self.Root is None:
            return 0
        return count_leaves(self.Root, 0)
