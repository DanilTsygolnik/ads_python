class SimpleTree:

    def __init__(self, Node=None):
        self.root = Node


    def AddChild(self, ParentNode, NewChild):

        ParentNode.Children.append(NewChild) # записать новый узел в список детей parent'а
        NewChild.Parent = ParentNode # обновить значение NodeLevel у NewChild


    def DeleteNode(self, NodeToDelete):

        if NodeToDelete.IsRoot:
            raise ValueError('This node is root. Choose another one.') # проверка, не является ли корневым
        NodeToDelete.Parent.Children.remove(NodeToDelete) # удалить NodeToDelete из списка parent.children
        NodeToDelete.Parent = None # удалить узел со всей веткой из дерева


    def GetAllNodes(self):

        def get_children_list(tmp_product:list, current_node):
            result = tmp_product
            if current_node.Children != []:
                for i in current_node.Children:
                    result = get_children_list(result+[i], i)
            return result

        return get_children_list([], self.root)


    def FindNodesByValue(self, val):
        pass


    def MoveNode(self, OriginalNode, NewParent):
        pass


    def Count(self):
        pass


    def LeafCount(self):
        pass


#----------------------------------------------------------------


    def GetAllNodes(self):
        """Вывести список всех узлов в произвольном порядке 

        Что нужно сделать:
        создать пустой список всех узлов
        пройти по каждому узлу, проверяя список Children
            пустой список -- предельный случай
            если не пустой -- вызвать рекурсивную функцию от каждого узла в списке, результат прибавить к общему списку узлов

        Returns
        -------
        list
            Список всех узлов в дереве
        """

        def get_children_list(tmp_product:list, current_node):
            result = tmp_product
            if current_node.Children != []:
                for i in current_node.Children:
                    result = get_children_list(result+[i], i)
            return result

        return get_children_list([], self.root)

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
