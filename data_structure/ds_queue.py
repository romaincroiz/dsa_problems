from typing import TypeVar, Generic

from data_structure.common.node import Node, get_node_value

T = TypeVar('T')


def node_value(node: Node | None):
    if node is None:
        return None
    return node.data


def check_valid_data(data: T):
    # To avoid confusion when dequeue / peak
    # we explicitly not support None value
    # That way, returning None from dequeue / peak
    # means: no Node at the front of the queue
    if data is None:
        raise Exception('Data invalid: cannot be None')


class DsQueue(Generic[T]):
    __front: Node = None
    __back: Node = None

    def is_empty(self) -> bool:
        return self.__front is None

    def peak(self) -> T:
        return node_value(self.__front)

    def enqueue(self, item: T):
        check_valid_data(item)
        node = Node(item)
        if self.is_empty():
            self.__set_front(node)
            self.__set_back(node)
        else:
            self.__back.next = node
            self.__set_back(node)

    def __set_back(self, node):
        self.__back = node

    def __set_front(self, node):
        self.__front = node

    def dequeue(self) -> T:
        if self.is_empty():
            raise Exception('Cannot dequeue: queue is empty')
        if self.__front == self.__back:
            self.__set_back(None)
        return self.__remove_at_front()

    def __remove_at_front(self) -> T:
        removed = self.__front
        self.__set_front(self.__front.next)
        removed.next = None
        return get_node_value(removed)

    def __str__(self) -> str:
        # front -> 1 -> 2 -> 3 -> 4 -> rear
        if self.is_empty():
            return "None"
        s = '(Front) -> '
        current = self.__front
        while current:
            s += f'{str(current)} -> '
            current = current.next
        s += '(Back)'
        return s
