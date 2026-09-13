import pytest

from data_structure.ds_min_heap import DsMinHeap, parent_index


class TestDsMinHeapNavigation:
    def test_is_parent_root_is_none(self):
        assert parent_index(0) is None

    def test_is_parent_even_index(self):
        assert parent_index(2) == 0
        assert parent_index(6) == 2
        assert parent_index(8) == 3

    def test_is_parent_odd_index(self):
        assert parent_index(1) == 0
        assert parent_index(5) == 2
        assert parent_index(13) == 6

class TestDsMinHeap:

    def test_peak_when_empty(self):
        heap = DsMinHeap()
        assert heap.peak() is None

    def test_peak_when_not_empty(self):
        heap = DsMinHeap()
        heap.add(5)
        assert heap.peak() is not None

    def test_peak_when_after_poll(self):
        heap = DsMinHeap()
        heap.add(5)
        heap.poll()
        assert heap.peak() is None

    def test_is_empty_after_init(self):
        heap = DsMinHeap()
        assert heap.is_empty() == True

    def test_is_not_empty_after_add(self):
        heap = DsMinHeap()
        heap.add(5)
        assert heap.is_empty() == False

    def test_is_empty_after_poll(self):
        heap = DsMinHeap()
        heap.add(6)
        heap.add(5)
        heap.poll()
        heap.poll()
        assert heap.is_empty() == True

    def test_is_empty_after_remove(self):
        heap = DsMinHeap()
        heap.add(1)
        heap.add(2)
        heap.remove(2)
        heap.remove(1)
        assert heap.is_empty() == True

    def test_one_element_after_add(self):
        heap = DsMinHeap()
        heap.add(7)
        assert heap.__str__() == '[7]'

    def test_in_expected_order_after_add(self):
        heap = DsMinHeap()
        heap.add(5)
        heap.add(1) # swap with 5
        heap.add(2) # stay in position
        assert heap.__str__() == '[1, 5, 2]'

    def test_poll_when_empty(self):
        heap = DsMinHeap()
        with pytest.raises(IndexError):
            heap.poll()

    def test_no_values_after_poll(self):
        heap = DsMinHeap()
        heap.add(5)
        heap.poll()
        assert heap.__str__() == '[]'

    def test_in_expected_order_after_poll(self):
        heap = DsMinHeap()
        heap.add(5) # 5
        heap.add(1) # 1, 5
        heap.add(2) # 1, 5, 2
        heap.poll() # 2, 5
        assert heap.__str__() == '[2, 5]'

    def test_remove_when_empty(self):
        heap = DsMinHeap()
        with pytest.raises(ValueError):
            heap.remove(5)

    def test_remove_when_not_found(self):
        heap = DsMinHeap()
        heap.add(2)

        with pytest.raises(ValueError):
            heap.remove(5)

    def test_remove_expected_order(self):
        heap = DsMinHeap()
        heap.add(5) # 5
        heap.add(3) # 3, 5
        heap.add(2) # 2, 5, 3
        heap.add(1) # 1, 2, 3, 5
        heap.remove(1) # 2, 5, 3
        heap.remove(3) # 2, 5
        assert heap.__str__() == '[2, 5]'