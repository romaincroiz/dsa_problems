from typing import Any


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class DsLinkedList:
    head = None
    size = 0

    def __str__(self):
        s = '['
        current_node = self.head
        is_first = True
        while current_node:
            if is_first:
                is_first = False
            else:
                s += ' -> '
            s += str(current_node)
            current_node = current_node.next
        s += ']'
        return s

    def get(self, position):
        self.__check_in_range(position)
        if position == 0:
            return self.head
        current_node = self.__get_node_before(position)
        return current_node.next

    def __check_in_range(self, index) -> bool | Any:
        if not(0 <= index <= self.size):
            raise Exception('index out of range')

    def __get_node_before(self, position) -> Any:
        # iterate until just before the position
        current_node = self.head
        for i in range(0, position - 1):
            current_node = current_node.next
        return current_node

    def remove_first(self, data):
        if self.is_empty() or data is None:
            return False
        return self.__find_and_remove_first(data)

    def __find_and_remove_first(self, data) -> bool:
        # Head: no need to iterate
        if self.head.data == data:
            self.__remove_head()
            return True

        return self.__iterate_and_remove_first(data)

    def __iterate_and_remove_first(self, data) -> bool:
        current_node = self.head
        next_node = self.head.next
        while next_node:
            if next_node.data == data:
                current_node.next = next_node.next
                self.__decrement_size()
                return True
            current_node = next_node
            next_node = next_node.next
        return False

    def remove_at(self, position):
        self.__check_in_range(position)
        if position == 0:
            self.__remove_head()
        else:
            current_node = self.__get_node_before(position)
            self.__remove(current_node, current_node.next)

    def __remove_head(self):
        if self.is_empty():
            return
        self.__remove(None, self.head)

    def __remove(self, prev_node, node_to_delete):
        if node_to_delete is None:
            return
        if prev_node is None:
            # head removed
            self.head = self.head.next
        else:
            prev_node.next = node_to_delete.next
            node_to_delete.next = None
        self.__decrement_size()

    def add(self, data, position):
        self.__check_in_range(position)

        new_node = Node(data)
        if position == 0:
            self.__insert(None, new_node)
        else:
            current_node = self.__get_node_before(position)
            self.__insert(current_node, new_node)

    def __insert(self, previous_node, new_node):
        if previous_node is None:
            # new node becomes head
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = previous_node.next
            previous_node.next = new_node
        self.__increment_size()

    def is_empty(self) -> Any:
        return self.size == 0

    def clear(self):
        self.head = None
        self.size = 0

    def __decrement_size(self):
        self.size -= 1

    def __increment_size(self):
        self.size += 1

def test_linked_list():
    ds = DsLinkedList()

    ds.add("apple", 0)
    print(ds) # [apple]
    ds.add("orange", 0)
    print(ds) # [orange->apple]
    ds.add("strawberry", 1)
    print(ds) # [orange->strawberry->apple]
    print(f'Node at position 2: {ds.get(2)}')
    ds.add("banana", 2)
    print(ds) # [orange->strawberry->banana->apple]
    ds.add("strawberry", 3)
    print(ds) # [orange->strawberry->banana->strawberry->apple]
    print(f'Node at position 3: {ds.get(3)}')
    ds.remove_first("not found")
    print(ds) # unchanged
    ds.remove_first("strawberry")
    print(ds) # [orange->banana->strawberry->apple]
    ds.remove_first("strawberry")
    print(ds) # [orange->banana->apple]
    ds.remove_first("strawberry")
    print(ds) # unchanged
    ds.remove_at(0)
    print(ds) # [banana->apple]
    ds.remove_at(1)
    print(ds) # [banana]
    ds.add("pineapple", 0)
    ds.add("tomato", 0)
    print(ds) # [tomato->pineapple->banana]
    print(f'Node at position 0: {ds.get(0)}')
    ds.clear()
    print(ds) # []

test_linked_list()