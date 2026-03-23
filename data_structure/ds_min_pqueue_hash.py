from typing import TypeVar, Generic

T = TypeVar('T')


def replace_index(indexes: set[int], ind_from, ind_to):
    indexes.remove(ind_from)
    indexes.add(ind_to)

def parent_index(child_ind):
    if child_ind == 0:
        raise IndexError('Index out of bounds')
    if child_ind <= 2:
        return 0
    if child_ind % 2 == 0:
        return child_ind // 2 - 1
    return child_ind // 2


def left_child_index(parent: int) -> int:
    return 2 * parent + 1


def right_child_index(parent: int) -> int:
    return 2 * parent + 2


class DsMinPriorityQueue(Generic[T]):
    """
    Implementation of Min priority queue with Hashtable
    """
    __heap: list[T]
    __map_value_to_indexes: dict[T, set[int]]

    def __init__(self):
        self.__heap = []
        self.__map_value_to_indexes = {}

    def __len__(self) -> int:
        return len(self.__heap)

    def clear(self):
        self.__map_value_to_indexes.clear()
        self.__heap.clear()

    def peak(self) -> T:
        if len(self) == 0:
            return None
        return self.__heap[0]

    def remove_min(self) -> T:
        return self._remove_at(0)

    def remove(self, element: T) -> T:
        if element not in self.__map_value_to_indexes:
            raise Exception('Element not in map')
        first_ind = next(iter(self.__map_value_to_indexes[element]))
        return self._remove_at(first_ind)

    def _remove_at(self, index: int) -> T:
        if len(self) == 0:
            raise Exception(f'Cannot remove element: priority queue is empty')
        # only swap if more than 1 item
        if len(self) > 1:
            self._swap(index, len(self) - 1)
        removed = self.__heap.pop()
        self.__remove_from_map(removed, len(self))
        self._sink_or_swim(index)
        return removed

    def _swap(self, source_index, target_index) -> None:
        source = self.__heap[source_index]
        target = self.__heap[target_index]

        if source != target:
            # swap indexes in map
            replace_index(self.__map_value_to_indexes[source], source_index, target_index)
            replace_index(self.__map_value_to_indexes[target], target_index, source_index)

            # swap values in heap
            self.__heap[source_index] = target
            self.__heap[target_index] = source

    def __remove_from_map(self, elt: T, index: int):
        if elt not in self.__map_value_to_indexes:
            raise Exception('Element not in map')
        else:
            indexes = self.__map_value_to_indexes.pop(elt)
            indexes.remove(index)
            if len(indexes) > 0:
                self.__map_value_to_indexes[elt] = indexes

    def _sink_or_swim(self, ind: int) -> None:
        if ind == 0:
            self._sink(ind)
        else:
            parent_ind = parent_index(ind)
            if self.is_heap_invariant_respected(parent_ind, ind):
                self._sink(ind)
            else:
                self._swim(ind)
        pass

    def _sink(self, ind: int) -> None:
        """
        Bubble down value at given index
        """
        left_ind = left_child_index(ind)
        right_ind = right_child_index(ind)
        if not self.is_heap_invariant_respected(ind, left_ind):
            self._swap(ind, left_ind)
            self._sink(left_ind)
        elif not self.is_heap_invariant_respected(ind, right_ind):
            self._swap(ind, right_ind)
            self._sink(right_ind)

    def _swim(self, ind: int) -> None:
        """
        Bubble up value at given index
        """
        if ind > 0:
            parent_ind = parent_index(ind)
            if not self.is_heap_invariant_respected(parent_ind, ind):
                self._swap(parent_ind, ind)
                self._swim(parent_ind)

    def insert(self, elt: T) -> None:
        last_index = len(self.__heap)
        self.__heap.append(elt)
        self.__add_to_map(elt, last_index)
        self._swim(last_index)

    def is_heap_invariant_respected(self, parent_ind, child_ind):
        if child_ind < len(self.__heap):
            return self.__heap[parent_ind] <= self.__heap[child_ind]
        return True

    def __add_to_map(self, elt: T, index: int):
        if elt not in self.__map_value_to_indexes:
            self.__map_value_to_indexes[elt] = {index}
        else:
            indexes = self.__map_value_to_indexes[elt]
            indexes.add(index)
