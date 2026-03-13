from typing import TypeVar, Generic

from data_structure.common.node import Node, get_node_value

T = TypeVar('T')

def check_valid_data(data: T):
    # To avoid confusion when getting data of a node / head
    # we explicitly not support None value
    # That way, returning None from get / peak
    # means: no Node at that position
    if data is None:
        raise Exception('Data invalid: cannot be None')

class DsLinkedList(Generic[T]):
    __head = None
    __size = 0

    def __str__(self):
        s = 'None'
        current_node = self.__head
        is_first = True
        while current_node:
            if is_first:
                is_first = False
                s = ''
            else:
                s += ' -> '
            s += str(current_node)
            current_node = current_node.next
        return s

    def get(self, position: int) -> Node | None:
        self.__check_element_in_range(position)
        current_node = self.__head
        if position == 0:
            return get_node_value(current_node)
        current_node = self.__get_node_before(position)
        return get_node_value(current_node.next)

    def __check_element_in_range(self, index: int):
        if not (0 <= index < len(self)):
            raise IndexError

    def __get_node_before(self, position: int) -> Node | None:
        # iterate until just before the position
        current_node = self.__head
        for i in range(0, position - 1):
            current_node = current_node.next
        return current_node

    def remove_first(self, data: T) -> bool:
        self.__check_can_do_remove()
        check_valid_data(data)
        return self.__find_and_remove_first(data)

    def __check_can_do_remove(self):
        if self.is_empty():
            raise Exception('Cannot remove: list is empty')

    def __find_and_remove_first(self, data: T) -> bool:
        # Head: no need to iterate
        if self.__head.data == data:
            self.__remove_head()
            return True

        return self.__iterate_and_remove_first(data)

    def __iterate_and_remove_first(self, data: T) -> bool:
        current_node = self.__head
        next_node = self.__head.next
        while next_node:
            if next_node.data == data:
                self.__remove_node(current_node, next_node)
                return True
            current_node = next_node
            next_node = current_node.next
        return False

    def remove_at(self, position: int) -> bool:
        self.__check_can_do_remove()
        self.__check_element_in_range(position)
        if position == 0:
            return self.__remove_head()
        else:
            current_node = self.__get_node_before(position)
            return self.__remove_node(current_node, current_node.next)

    def __remove_head(self) -> bool:
        return self.__remove_node(None, self.__head)

    def __remove_node(self, prev_node: Node | None, node_to_delete: Node) -> bool:
        if prev_node is None:
            # __head removed
            self.__head = self.__head.next
        else:
            prev_node.next = node_to_delete.next
            node_to_delete.next = None
        self.__decrement_size()
        return True

    def add(self, position: int, data: T):
        self.__check_add_in_range(position)
        check_valid_data(data)

        node_to_insert = Node(data)
        if position == 0:
            self.__insert_node_after(None, node_to_insert)
        else:
            previous_node = self.__get_node_before(position)
            self.__insert_node_after(previous_node, node_to_insert)

    def __check_add_in_range(self, add_index: int):
        if add_index > len(self) or add_index < 0:
            raise IndexError

    def __insert_node_after(self, previous_node: Node | None, node_to_insert: Node):
        if previous_node is None:
            # new node becomes __head
            node_to_insert.next = self.__head
            self.__head = node_to_insert
        else:
            node_to_insert.next = previous_node.next
            previous_node.next = node_to_insert
        self.__increment_size()

    def __len__(self) -> int:
        return self.__size

    def peak(self) -> Node | None:
        return get_node_value(self.__head)

    def is_empty(self) -> bool:
        return len(self) == 0

    def clear(self):
        self.__head = None
        self.__size = 0

    def __decrement_size(self):
        self.__size -= 1

    def __increment_size(self):
        self.__size += 1
