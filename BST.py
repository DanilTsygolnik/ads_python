# pylint: disable=c0103,c0114,c0115,c0116,c0301,r0903

class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


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
        # добавляем ключ-значение в дерево
        return False # если ключ уже есть


    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        return None


    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        return False # если узел не найден


    def Count(self):
        return 0 # количество узлов в дереве
