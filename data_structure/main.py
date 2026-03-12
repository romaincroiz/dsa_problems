from data_structure.ds_dynamic_array import DsDynamicArray
from data_structure.ds_linked_list import DsLinkedList
from data_structure.ds_stack import DsStack


def test_array():
    print('==== TEST ARRAY ====')

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

def test_linked_list():
    print('==== TEST LINKED LIST ====')

    ll = DsLinkedList()

    ll.add("apple", 0)
    print(ll) # [apple]
    print('head:', ll.peak()) # apple

    ll.add("orange", 0)
    print(ll) # [orange->apple]
    print('head:', ll.peak())  # orange

    ll.add("strawberry", 1)
    print(ll) # [orange->strawberry->apple]
    print(f'Node at position 2: {ll.get(2)}')

    ll.add("banana", 2)
    print(ll) # [orange->strawberry->banana->apple]

    ll.add("strawberry", 3)
    print(ll) # [orange->strawberry->banana->strawberry->apple]
    print(f'Node at position 3: {ll.get(3)}')
    ll.remove_first("not found")
    print(ll) # unchanged

    ll.remove_first("strawberry")
    print(ll) # [orange->banana->strawberry->apple]

    ll.remove_first("strawberry")
    print(ll) # [orange->banana->apple]
    ll.remove_first("strawberry")
    print(ll) # unchanged

    ll.remove_at(0)
    print(ll) # [banana->apple]

    ll.remove_at(1)
    print(ll) # [banana]

    ll.add("pineapple", 0)
    ll.add("tomato", 0)
    print(ll) # [tomato->pineapple->banana]
    print(f'Node at position 0: {ll.get(0)}')
    print('isEmpty ?:', ll.is_empty())  # False

    ll.clear()
    print('isEmpty ?:', ll.is_empty())  # True
    print(ll) # []

def test_stack():
    print('==== TEST STACK ====')
    s = DsStack()

    s.push("apple")
    print(s) # [apple]
    print('head:', s.peak()) # ->apple

    s.push("orange")
    print(s) # [->orange->apple]
    print('head:', s.peak())  # orange

    s.push("strawberry")
    print(s) # # [->strawberry->orange->apple]

    print(f'pop {s.pop()}') # strawberry
    print(s) # [->orange->apple]

    print(f'pop {s.pop()}')  # orange
    print(s)  # [->apple]

    s.push("pineapple")
    print(s) # [->pineapple->apple]

    print('isEmpty ?:', s.is_empty())  # False
    s.clear()
    print('isEmpty ?:', s.is_empty())  # True
    print(s) # []

if __name__ == '__main__':
    test_array()
    test_linked_list()
    test_stack()
