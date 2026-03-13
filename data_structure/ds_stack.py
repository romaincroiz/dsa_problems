from typing import TypeVar, Generic

from data_structure.common.node import Node, get_node_value

T = TypeVar("T")

def check_valid_data(data: T):
    # To avoid confusion when peak / pop
    # we explicitly not support None value
    # That way, returning None from pop / peak
    # means: the stack is empty
    if data is None:
        raise Exception('Data invalid: cannot be None')

class DsStack(Generic[T]):
    __top: Node = None

    def push(self, data: T):
        check_valid_data(data)
        self.__push_node_on_top(Node(data))

    def __push_node_on_top(self, node: Node):
        node.next = self.__top
        self.__set_top_node(node)

    def __set_top_node(self, node: Node):
        self.__top = node

    def peak(self) -> Node | None:
        return get_node_value(self.__top)

    def pop(self) -> T:
        if self.is_empty():
            raise Exception('Stack is empty')
        popped = self.__top
        self.__set_top_node(popped.next)
        popped.next = None

        return popped.data

    def clear(self):
        while not self.is_empty():
            self.pop()

    def is_empty(self) -> bool:
        return self.__top is None

    def __str__(self) -> str:
        if self.is_empty():
            return 'None'
        s = '(Top)'
        current_node = self.__top
        while current_node:
            s += f' -> {current_node}'
            current_node = current_node.next
        return s
