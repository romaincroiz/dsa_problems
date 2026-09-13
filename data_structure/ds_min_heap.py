def left_child_index(parent_ind: int) -> int:
    return parent_ind * 2 + 1

def right_child_index(parent_ind: int) -> int:
    return parent_ind * 2 + 2

def parent_index(index: int) -> int | None:
    if index == 0:
        return None
    if index % 2 == 0:
        return index // 2 -1
    return index // 2

class DsMinHeap:

    __heap: list[int]

    def __init__(self):
        self.__heap = []

    def __str__(self) -> str:
        return str(self.__heap)

    def peak(self) -> int | None:
        if self.is_empty():
            return None
        return self.__heap[0]

    def is_empty(self) -> bool:
        return len(self.__heap) == 0

    def add(self, value: int) -> None:
        self.__heap.append(value)
        self._swim(len(self.__heap) - 1)

    def _swim(self, last_index: int):
        parent = parent_index(last_index)

        while parent is not None and not self._is_lower(parent, last_index):
            self._swap(parent, last_index)
            last_index = parent
            parent = parent_index(last_index)

    def poll(self) -> int:
        if self.is_empty():
            raise IndexError('Cannot poll, heap is empty')
        self._swap(0, len(self.__heap) - 1)
        polled = self.__heap.pop(len(self.__heap) - 1)

        self._sink(0)
        return polled

    def _sink(self, last_index: int):

        while True:
            left = left_child_index(last_index)
            right = right_child_index(last_index)

            if left >= len(self.__heap) or not self._is_lower(left, last_index):
                # value at the right position, abort
                return

            min_value_index = left

            if right < len(self.__heap) and not self._is_lower(left, right):
                min_value_index = right
            # swap with the lowest between left / right
            self._swap(last_index, min_value_index)
            last_index = min_value_index

    def _swap(self, first_index: int, second_index: int):
        self._check_in_bound([first_index, second_index])

        if first_index == second_index:
            return
        else:
            first = self.__heap[first_index]
            self.__heap[first_index] = self.__heap[second_index]
            self.__heap[second_index] = first

    def remove(self, value: int) -> int | None:
        first_index = self.__heap.index(value)
        end_index = len(self.__heap) - 1
        self._swap(first_index, end_index)
        removed = self.__heap.pop(len(self.__heap) - 1)

        # nothing to reposition if the removed item was already at the end
        if first_index != end_index:
            self._sink_or_swim(first_index)

        return removed

    def _is_lower(self, left_operand_ind: int, right_operand_ind) -> bool:
        self._check_in_bound([left_operand_ind, right_operand_ind])
        return (right_operand_ind == left_operand_ind or
                self.__heap[left_operand_ind] <= self.__heap[right_operand_ind])

    def _check_in_bound(self, indexes:list[int]) -> None:
        for index in indexes:
            if index < 0 or index >= len(self.__heap):
                raise IndexError('Index out of bounds')

    def _sink_or_swim(self, index):
        self._swim(index)
        self._sink(index)