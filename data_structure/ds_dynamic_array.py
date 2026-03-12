MIN_MEMORY = 2

def static_array(length=MIN_MEMORY):
    """ Helper function for static array. """
    if length < MIN_MEMORY:
        length = MIN_MEMORY
    return [None] * length

# As python already handles arrays dynamically,
# we 'emulate' static arrays by handling
# the 'memory' and 'size' of the array
class DsDynamicArray:

    __default_memory = MIN_MEMORY
    __memory = 0
    __inner_array = []
    __size = 0

    def __init__(self, length=MIN_MEMORY):
        self.__default_memory = length
        self.__initialize()

    def __initialize(self):
        # allocate 'empty' spaces
        self.__inner_array = static_array(self.__default_memory)
        self.__memory = self.__default_memory
        self.__size = 0

    def clear(self):
        self.__initialize()

    def get(self, index):
        self.__check_in_range(index)
        return self.__inner_array[index]

    def __check_in_range(self, index):
        if index < 0 or index >= self.__size:
            raise Exception('index out of range')

    def __len__(self):
        return self.__size

    def append(self, element):
        """ Add element to the end of the array. """
        self.insert(self.__size, element)

    def insert(self, index, element):
        """ Add element to the end of the array. """
        self.__reallocate_memory()
        self.__increment_size()
        self.__inner_array.insert(index, element)

    def remove(self, index):
        self.__check_in_range(index)
        return self.__remove_at(index)

    def __remove_at(self, index):
        element = self.__inner_array.pop(index)
        self.__decrement_size()
        self.__reallocate_memory()
        return element

    def __increment_size(self):
        self.__size += 1

    def __decrement_size(self):
        self.__size -= 1

    def __reallocate_memory(self):
        if self.__no_available_memory():
            # allocate new memory to the array
            self.__expand_memory()
        elif self.__is_shrinkable():
            # reduce memory used by the array
            self.__shrink_memory()

    def __no_available_memory(self) -> bool:
        return self.__size >= self.__memory

    def __is_shrinkable(self) -> bool:
        return self.__size < self.__memory // 2

    def __expand_memory(self):
        self.__update_memory(self.__memory * 2)
        self._reallocate_array()

    def __shrink_memory(self):
        self.__update_memory(self.__memory // 2)
        self._reallocate_array()

    def __update_memory(self, new_value):
        if new_value < MIN_MEMORY:
            new_value = MIN_MEMORY
        self.__memory = new_value

    def _reallocate_array(self):
        new_array = static_array(self.__memory)

        for i in range(0, self.__size):
            new_array[i] = self.__inner_array[i]
        self.__inner_array = new_array

    def __str__(self):
        return f'inner array: {self.__inner_array}, size: {self.__size}, memory: {self.__memory}'

def test_array():
    dyn_array = DsDynamicArray()
    dyn_array.append(1)
    print(dyn_array)

    dyn_array.append(2)
    print(dyn_array)

    dyn_array.append(3)
    print(dyn_array)

    print(f'inserting 4 at pos 1...')
    dyn_array.insert(1, 4)
    print(dyn_array)

    print(f'removing {dyn_array.remove(3)}...')
    print(dyn_array)

    print(f'removing {dyn_array.remove(1)}...')
    print(dyn_array)

    print(f'clearing...')
    dyn_array.clear()
    print(dyn_array)