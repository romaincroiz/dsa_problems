from data_structure.common.node import Node


class DsLinkedList:
    __head = None
    __size = 0

    def __str__(self):
        s = '['
        current_node = self.__head
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
            return self.__head
        current_node = self.__get_node_before(position)
        return current_node.next

    def __check_in_range(self, index):
        if not(0 <= index <= len(self)):
            raise Exception('index out of range')

    def __get_node_before(self, position) -> Node:
        # iterate until just before the position
        current_node = self.__head
        for i in range(0, position - 1):
            current_node = current_node.next
        return current_node

    def remove_first(self, data) -> bool:
        if self.is_empty() or data is None:
            return False
        return self.__find_and_remove_first(data)

    def __find_and_remove_first(self, data) -> bool:
        # Head: no need to iterate
        if self.__head.data == data:
            self.__remove_head()
            return True

        return self.__iterate_and_remove_first(data)

    def __iterate_and_remove_first(self, data) -> bool:
        current_node = self.__head
        next_node = self.__head.next
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
        self.__remove(None, self.__head)

    def __remove(self, prev_node, node_to_delete):
        if node_to_delete is None:
            return
        if prev_node is None:
            # __head removed
            self.__head = self.__head.next
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
            # new node becomes __head
            new_node.next = self.__head
            self.__head = new_node
        else:
            new_node.next = previous_node.next
            previous_node.next = new_node
        self.__increment_size()

    def __len__(self):
        return self.__size

    def peak(self):
        if not self.is_empty():
            return self.__head
        return None

    def is_empty(self) -> bool:
        return len(self) == 0

    def clear(self):
        self.__head = None
        self.__size = 0

    def __decrement_size(self):
        self.__size -= 1

    def __increment_size(self):
        self.__size += 1