# pylint: disable=c0103,c0114,c0115,c0116,c0301,r0903

class BSTNode:

    def __init__(self, key, val=None, parent=None):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.is_orphan = (self.LeftChild is None) and (self.RightChild is None)

    def replace_with(self, node, pass_kids_on=False):
        if isinstance(node, BSTNode):
            node.replace_with(None)
            node.Parent = self.Parent
        if isinstance(self.Parent, BSTNode):
            self_is_left_child = (self.Parent.LeftChild is self)
            if self_is_left_child:
                self.Parent.LeftChild = node
            else:
                self.Parent.RightChild = node
            self.Parent = None
        if pass_kids_on:
            node.LeftChild = self.LeftChild
            node.RightChild = self.RightChild
            if self.LeftChild is not None:
                self.LeftChild.Parent = node
            if self.RightChild is not None:
                self.RightChild.Parent = node
            self.LeftChild = None
            self.RightChild = None


class BSTFind: # промежуточный результат поиска

    def __init__(self, node=None, has_key=False, to_left=False):
        self.Node = node          # None если в дереве вообще нету узлов
        self.NodeHasKey = has_key # True если узел найден
        self.ToLeft = to_left     # True, если родительскому узлу надо
                                  # добавить новый узел левым потомком

class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None

    def FindNodeByKey(self, key):

        def search_func(key, node):
            """ищем в дереве узел и сопутствующую информацию по ключу"""

            if node is not None: # в дереве есть узлы
                if key == node.NodeKey:                     # нужный ключ найден
                    return BSTFind(node, True, False)
                # искомый ключ меньше текущего
                if key < node.NodeKey:
                    if node.LeftChild is None:              # есть левый слот под узел с искомым ключом
                        return BSTFind(node, False, True)
                    return search_func(key, node.LeftChild) # левый слот занят, спускаемся ниже
                # искомый ключ больше текущего
                if node.RightChild is None:                 # есть правый слот под узел с искомым ключом
                    return BSTFind(node, False, False)
                return search_func(key, node.RightChild)    # правый слот занят, спускаемся ниже
            return BSTFind() # в дереве нет узлов


        return search_func(key, self.Root) # поиск ключа, начиная с корня дерева


    def AddKeyValue(self, key, val):
        """добавляем ключ-значение в дерево"""

        key_search_result = self.FindNodeByKey(key)
        if key_search_result.NodeHasKey: # если ключ уже есть
            return False
        new_node = BSTNode(key, val, None)
        if key_search_result.Node is None: # если дерево пустое
            self.Root = new_node
        else:
            new_node.Parent = key_search_result.Node
            if key_search_result.ToLeft:
                key_search_result.Node.LeftChild = new_node
            else:
                key_search_result.Node.RightChild = new_node
        return True


    def FindMinMax(self, FromNode, FindMax):
        if isinstance(FromNode, BSTNode):
            if FindMax:
                if FromNode.RightChild is None:
                    return FromNode
                return self.FindMinMax(FromNode.RightChild, True)
            if FromNode.LeftChild is None:
                return FromNode
            return self.FindMinMax(FromNode.LeftChild, False)
        return None


    def Count(self):
        def count_nodes_from(node):
            if isinstance(node, BSTNode):
                return 1 + count_nodes_from(node.LeftChild) + \
                           count_nodes_from(node.RightChild)
            return 0

        return count_nodes_from(self.Root)


    def DeleteNodeByKey(self, key):
        search_result = self.FindNodeByKey(key)
        if search_result.NodeHasKey:
            node_to_delete = search_result.Node
            if node_to_delete.RightChild is not None:
                in_subtree = node_to_delete.RightChild
                heir = self.FindMinMax(in_subtree, FindMax=False)
                if heir.is_orphan:
                    heir_placeholder = heir.RightChild
                    heir.replace_with(heir_placeholder)
                pass_kids_on = True
            if node_to_delete.RightChild is None:
                if node_to_delete.LeftChild is not None:
                    heir = node_to_delete.LeftChild
                else:
                    heir = None
                pass_kids_on = False
            node_to_delete.replace_with(heir, pass_kids_on)
            if node_to_delete is self.Root:
                self.Root = heir
            return True
        return False
