class SimpleTree:

    def MoveNode(self, OriginalNode, NewParent):
        """Переместить некорневой узел дочерним узлом в другое место дерева (вместе с его поддеревом)

        Что нужно:
        - [ ] воспользоваться методом delete_node(node)
        - [ ] записать в node.parent значение destination.node_id
        - [ ] добавить node.node_id в список destination.children
        

        Parameters
        ----------
        OriginalNode : SimpleTreeNode.leaf_id
            Указатель на текущий узел
        NewParent : SimpleTreeNode.leaf_id
            Указатель на новое место в дереве, куда переносим узел с поддеревом
        """
