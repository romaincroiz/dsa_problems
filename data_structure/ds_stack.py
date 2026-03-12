from data_structure.common.node import Node


class DsStack:
    __top: Node = None

    def push(self, data):
        self.__push_on_top(Node(data))

    def __push_on_top(self, node):
        node.next = self.__top
        self.__set_top(node)

    def __set_top(self, node):
        self.__top = node

    def peak(self) -> Node | None:
        if self.is_empty():
            return None
        return self.__top

    def pop(self) -> Node:
        if self.is_empty():
            raise Exception('Stack is empty')
        popped = self.peak()
        self.__set_top(popped.next)
        return popped

    def clear(self):
        while not self.is_empty():
            self.pop()

    def is_empty(self):
        return self.__top is None

    def __str__(self):
        s = '['
        current_node = self.peak()
        while current_node:
            s += f' -> {current_node}'
            current_node = current_node.next
        s += ']'
        return s