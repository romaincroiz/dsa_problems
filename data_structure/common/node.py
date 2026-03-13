from typing import TypeVar, Generic

T = TypeVar('T')

def get_node_value(node: Node | None):
    if node:
        return node.data
    return None

class Node(Generic[T]):

    def __init__(self, data: object):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
