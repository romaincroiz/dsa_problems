# As python already handles arrays dynamically,
# we 'emulate' static arrays by handling
# the '_memory' and '_size' of the array
from typing import Any

MIN_MEMORY = 2

def static_array(length=MIN_MEMORY):
    """ Helper function for static array. """
    if length < MIN_MEMORY:
        length = MIN_MEMORY
    return [None] * length

class DsDynamicArray:

    _default_memory = MIN_MEMORY
    _memory = 0
    _inner_array = []
    _size = 0

    def __init__(self, length=MIN_MEMORY):
        self._default_memory = length
        self.__initialize()

    def __initialize(self):
        # allocate 'empty' spaces
        self._inner_array = static_array(self._default_memory)
        self._memory = self._default_memory
        self._size = 0

    def clear(self):
        self.__initialize()

    def get(self, index):
        self.__check_in_range(index)
        return self._inner_array[index]

    def __check_in_range(self, index) -> bool | Any:
        if index < 0 or index >= self._size:
            raise Exception('index out of range')

    def size(self):
        return self._size

    def append(self, element):
        """ Add element to the end of the array. """
        self.insert(self._size, element)

    def insert(self, index, element):
        """ Add element to the end of the array. """
        self.__reallocate_memory()
        self.__increment_size()
        self._inner_array.insert(index, element)

    def remove(self, index):
        self.__check_in_range(index)
        return self.__remove_at(index)

    def __remove_at(self, index):
        element = self._inner_array.pop(index)
        self.__decrement_size()
        self.__reallocate_memory()
        return element

    def __increment_size(self):
        self._size += 1

    def __decrement_size(self):
        self._size -= 1

    def __reallocate_memory(self):
        if self.__no_available_memory():
            # allocate new _memory to the array
            self.__expand_memory()
        elif self.__is_shrinkable():
            # reduce memory used by the array
            self.__shrink_memory()

    def __no_available_memory(self) -> bool:
        return self._size >= self._memory

    def __is_shrinkable(self) -> bool:
        return self._size < self._memory // 2

    def __expand_memory(self):
        self.__update_memory(self._memory * 2)
        self._reallocate_array()

    def __shrink_memory(self):
        self.__update_memory(self._memory // 2)
        self._reallocate_array()

    def __update_memory(self, new_value):
        if new_value < MIN_MEMORY:
            new_value = MIN_MEMORY
        self._memory = new_value

    def _reallocate_array(self):
        new_array = static_array(self._memory)

        for i in range(0, self._size):
            new_array[i] = self._inner_array[i]
        self._inner_array = new_array

    def __str__(self):
        return f'inner array: {self._inner_array}, size: {self._size}, memory: {self._memory}'


def test_array():

    ds = DsDynamicArray()
    ds.append(1)
    print(ds)
    ds.append(2)
    print(ds)
    ds.append(3)
    print(ds)
    print(f'inserting 4 at pos 1...')
    ds.insert(1, 4)
    print(ds)
    print(f'removing {ds.remove(3)}...')
    print(ds)
    print(f'removing {ds.remove(1)}...')
    print(ds)
    print(f'clearing...')
    ds.clear()
    print(ds)