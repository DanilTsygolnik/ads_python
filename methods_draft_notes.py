class SimpleTree:

    def DeleteNode(self, NodeToDelete):

        if NodeToDelete.IsRoot:
            raise ValueError('This node is root. Choose another one.') # проверка, не является ли корневым
        NodeToDelete.Parent.Children.remove(NodeToDelete) # удалить NodeToDelete из списка parent.children
        NodeToDelete.Parent = None # удалить узел со всей веткой из дерева


    def FindNodesByValue(self, val):
        """Найти список подходящих узлов по заданному значению

        Что нужно:
        - [ ] создать пустой список
        - [ ] перебрать все узлы в дереве, если мэтч -- добавить в список
        - [ ] вывести список найденных узлов

        Parameters
        ----------
        val : optional
            Параметр для поиска по значению
        """
        
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
