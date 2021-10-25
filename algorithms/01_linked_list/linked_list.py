# pylint: disable=c0103,c0114,r0903
class Node:
    """Класс для создания узлов связного списка"""
    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:
    """Класс для работы со связными списками"""
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        """Метод добавления нового узла в конец связного списка"""
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self, as_list=False):
        """
        Метод вывода значений всех узлов связного списка
        По умолчанию выводит на экран значение каждого узла
        При as_list=True возвращает список значений узлов
        """
        node = self.head
        nodes_values = []
        while node is not None:
            if as_list is False:
                print(node.value)
            nodes_values.append(node.value)
            node = node.next
        if as_list:
            return nodes_values

    def find(self, val):
        """Метод возвращает первый найденный по значению val узел"""
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    # ++ approved
    def delete(self, val, remove_all=False):
        """
        Метод удаления узлов по заданному значению val
        По умолчанию из списка удаляется только первый найденный узел
        При remove_all=True будут удалены все найденные узлы
        """
        curr_node = self.head
        prev_node = None
        while curr_node is not None:
            if curr_node.value == val:
                if curr_node is self.tail:
                    if prev_node is None:
                        self.clean()
                        break
                    prev_node.next = None
                    self.tail = prev_node
                elif curr_node.next.value != val:
                    if prev_node is None:
                        self.head = curr_node.next
                    else:
                        prev_node.next = curr_node.next
                        if remove_all is False:
                            break
                else:
                    if remove_all is False:
                        if prev_node is None:
                            self.head = curr_node.next
                        else:
                            prev_node.next = curr_node.next
                        break
            else:
                prev_node = curr_node
            curr_node = curr_node.next

    # ++ approved
    def find_all(self, val):
        """Метод возвращает список всех узлов со значением val"""
        results = []
        node = self.head
        while node is not None:
            if node.value == val:
                results.append(node)
            node = node.next
        return results

    # ++ approved
    def clean(self):
        """Метод удаления всех узлов"""
        self.head = None
        self.tail = None

    # ++ approved
    def len(self):
        """Метод возвращает кол-во узлов в связном списке"""
        cnt = 0
        node = self.head
        while node is not None:
            cnt += 1
            node = node.next
        return cnt

    # ready for approval
    def insert(self, afterNode, newNode):
        """Вставка нового узла newNode после заданного afterNode"""
        if (afterNode is not None) and (self.head is not None):
            node = self.head
            while node is not None:
                if node is afterNode: # вставляем, если искомый узел найден
                    newNode.next = node.next # связываем новый узел со следующим за текущим
                    node.next = newNode # связываем текущий узел со вставляемым
                    break # продолжать перебор смысла нет
                node = node.next
        else: # вставка в голову
            newNode.next = self.head # связать новый узел со следующим, т.е. с бывшей головой
            self.head = newNode # назначить узел головой
