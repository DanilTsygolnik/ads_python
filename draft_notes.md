Решение за O(1) заработает после добавления поля `self.num_nodes` в класс BST и апдейта методов BST.AddNodeByKey и BST.DeleteNodeByKey
```python
class BST:
    ...

    def Count(self):
        def count_nodes_from(node):
            if isinstance(node, BSTNode):
                return 1 + count_nodes_from(node.LeftChild) + \
                           count_nodes_from(node.RightChild)
            return 0

        if self.num_nodes is None:
            self.num_nodes = count_nodes_from(self.Root)
        return self.num_nodes
```
