from typing import TypeVar, Generic

T = TypeVar('T')

def parent_index(index: int) -> int:
    if index == 0:
        raise IndexError('Index out of bounds')
    if index <= 2:
        return 0
    if index % 2 == 0:
        return index // 2 - 1
    return index // 2

def left_child_index(parent_ind: int) -> int:
    return parent_ind * 2 + 1

def right_child_index(parent_ind: int) -> int:
    return parent_ind * 2 + 2


class DsMaxPriorityQueue(Generic[T]):
    """
        Implementation of Min priority queue with Hashtable
        """
    __heap: list[T]

    def __init__(self, elements: list):
        self.__heap = elements
        self._heapify()

    def __len__(self):
        return len(self.__heap)

    def clear(self):
        self.__heap = []

    def _heapify(self):
        """
        Heapify algorithm to build a priority queue from a list of elements.
        1. Insert the elements unordered
        2. Starting from the end, sink: If current element is lower than the max of its children, swap with
        the max of its children

        This algorithm has time complexity of O(n).
        """
        for i in range(len(self.__heap), -1, -1):
            self._sink(i)

    def insert(self, element: T):
        """
        Performs insertion by following these steps:
        1. Insert new element at the end of the priority queue
        2. Swim: While element > parent, swap with the parent

        This algorithm has time complexity of O(log n).
        """
        last_ind = len(self.__heap)
        self.__heap.append(element)
        self._swim(last_ind)

    def _swim(self, index):
        while index > 0:
            parent_ind = parent_index(index)
            if self.__heap[parent_ind] < self.__heap[index]:
                self._swap(index, parent_ind)
                index = parent_ind
            else:
                break
        pass

    def peak(self) -> T:
        if len(self.__heap) <= 0:
            return None
        return self.__heap[0]

    def remove_max(self) -> T:
        """
        Performs removal by following these steps:
        1. Swap root element with last element
        2. Remove the last element
        3. Sink the root element until the heap is valid

        This algorithm has time complexity of O(log n).
        """
        if len(self.__heap) <= 0:
            raise IndexError('Empty priority queue')
        if len(self.__heap) == 1:
            return self.__heap.pop(0)
        return self._remove_first_with_sink()

    def _remove_first_with_sink(self):
        self._swap(0, len(self.__heap) - 1)
        removed = self.__heap.pop(len(self.__heap) - 1)
        self._sink(0)
        return removed

    def _sink(self, index):
        """
        Performs swaps starting at the given index until element is greater than its children.

        1. Compares current element vs max of its children

        A1. If current element < max of its children, swap with the max of its children

        A2. Update current index to index of max of its children

        B. Otherwise, stop the sink (element is at correct position)
        """
        while self._has_child(index):
            max_child_ind = self._get_max_child_ind(index)

            if self.__heap[max_child_ind] > self.__heap[index]:
                self._swap(index, max_child_ind)
                index = max_child_ind
            else:
                # right position, abort
                break

    def _has_right_child(self, parent_ind: int) -> bool:
        return right_child_index(parent_ind) < len(self.__heap)

    def _has_left_child(self, parent_ind: int) -> bool:
        return left_child_index(parent_ind) < len(self.__heap)

    def _swapped_with_child(self, parent_ind, child_ind):
        if self.__heap[parent_ind] < self.__heap[child_ind]:
            self._swap(parent_ind, child_ind)
            return True
        return False

    def _swap(self, from_ind, to_ind):
        from_val = self.__heap[from_ind]
        self.__heap[from_ind] = self.__heap[to_ind]
        self.__heap[to_ind] = from_val

    def _has_child(self, parent_ind: int) -> bool:
        return self._has_left_child(parent_ind)

    def _get_max_child(self, parent_ind: int) -> T:
        return self.__heap[self._get_max_child_ind(parent_ind)]

    def _get_max_child_ind(self, parent_ind: int) -> int:
        if not self._has_left_child(parent_ind):
            raise Exception(f'Cannot find max child index: no child for index {parent_ind}')

        left = left_child_index(parent_ind)
        right = right_child_index(parent_ind)

        if not self._has_right_child(parent_ind) or self.__heap[left] > self.__heap[right]:
            return left
        return right