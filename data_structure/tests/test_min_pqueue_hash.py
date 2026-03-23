import pytest

from data_structure.ds_min_pqueue_hash import *


def check_priority_queue_content(priority_queue: DsMinPriorityQueue, expected_elements: list):
    assert len(priority_queue) == len(expected_elements)

    for i in range(len(priority_queue)):
        actual = priority_queue.remove_min()
        assert actual == expected_elements.pop(0)


class TestDsPriorityQueue:

    def setup_method(self):
        self.under_test = DsMinPriorityQueue()

    def test_parent_nav(self):
        with pytest.raises(IndexError):
            assert parent_index(0)
        assert parent_index(1) == 0
        assert parent_index(2) == 0
        assert parent_index(3) == 1
        assert parent_index(4) == 1
        assert parent_index(5) == 2
        assert parent_index(6) == 2
        assert parent_index(7) == 3
        assert parent_index(8) == 3

    def test_child_left_nav(self):
        assert left_child_index(0) == 1
        assert left_child_index(1) == 3
        assert left_child_index(2) == 5

    def test_child_right_nav(self):
        assert right_child_index(0) == 2
        assert right_child_index(1) == 4
        assert right_child_index(2) == 6

    def test_should_peak_return_none_when_empty(self):
        self.under_test.insert(99)
        self.under_test.insert(11)

        self.under_test.clear()
        assert len(self.under_test) == 0
        assert self.under_test.peak() is None

    def test_should_be_empty(self):
        assert len(self.under_test) == 0

    def test_should_not_be_empty_after_adding(self):
        self.under_test.insert(99)
        assert len(self.under_test) == 1
        check_priority_queue_content(self.under_test, [99])

    def test_should_be_min_priority_queue(self):
        self.under_test.insert(99)
        self.under_test.insert(11)
        self.under_test.insert(22)
        self.under_test.insert(22)
        self.under_test.insert(22)
        self.under_test.insert(1)

        self.under_test.remove(22)
        self.under_test.remove(11)

        assert len(self.under_test) == 4
        check_priority_queue_content(self.under_test, [1, 22, 22, 99])
