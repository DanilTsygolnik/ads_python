class SimpleTreeNode:
	"""
    
    Attributes
    ----------
    leaf_id : ??
        идентификатор листа, чтобы можно было ссылаться
    leaf_value : None, int, optional
        значение, которое хранится в листе (default is None)
    parent : SimpleTreeNode.leaf_id
        указатель на родительский узел
        желателен для быстрого выполнения различных операций
    children : []
        список дочерних узлов
    leaf_lvl : int
        поддержка уровня узлов без анализа всего дерева (extra task)

    """
    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов
	
