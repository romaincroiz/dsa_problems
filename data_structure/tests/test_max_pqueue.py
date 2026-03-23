from random import randint

import pytest

from data_structure.ds_max_pqueue import *


def check_priority_queue_content(priority_queue: DsMaxPriorityQueue, expected_elements: list):
    assert len(priority_queue) == len(expected_elements)

    for i in range(len(priority_queue)):
        actual = priority_queue.remove_max()
        assert actual == expected_elements.pop(0)


def init_rand_list(nb_elt):
    test_list = []
    for i in range(0, nb_elt):
        test_list.append(randint(0, 100000))
    return test_list


def init_priority_queue_with_heapify(unsorted_list):
    return DsMaxPriorityQueue(unsorted_list)


def init_priority_queue_without_heapify(unsorted_list):
    queue = DsMaxPriorityQueue([])
    for element in unsorted_list:
        queue.insert(element)
    return queue


class TestDsPriorityQueue:

    def test_parent_nav(self):
        with pytest.raises(Exception):
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
        self.under_test = DsMaxPriorityQueue([99, 11])

        self.under_test.clear()
        assert len(self.under_test) == 0
        assert self.under_test.peak() is None

    def test_should_not_be_empty_after_adding(self):
        self.under_test = DsMaxPriorityQueue([])
        self.under_test.insert(99)
        assert len(self.under_test) == 1
        check_priority_queue_content(self.under_test, [99])

    def test_should_heapify_and_be_valid_priority_queue(self):
        unsorted_list: list[int] = init_rand_list(100)
        self.under_test = init_priority_queue_with_heapify(unsorted_list.copy())
        unsorted_list.sort(reverse=True)

        check_priority_queue_content(self.under_test, unsorted_list)

    def test_should_insert_and_be_valid_priority_queue(self):
        unsorted_list: list[int] = init_rand_list(100)

        self.under_test = init_priority_queue_without_heapify(unsorted_list.copy())
        unsorted_list.sort(reverse=True)

        check_priority_queue_content(self.under_test, unsorted_list)

    def test_should_delete_and_be_valid_priority_queue(self):
        unsorted_list: list[int] = init_rand_list(100)
        self.under_test = init_priority_queue_with_heapify(unsorted_list.copy())
        unsorted_list.sort(reverse=True)

        assert self.under_test.remove_max() == unsorted_list.pop(0)
        assert self.under_test.remove_max() == unsorted_list.pop(0)
        assert self.under_test.remove_max() == unsorted_list.pop(0)
        assert self.under_test.remove_max() == unsorted_list.pop(0)
        assert self.under_test.remove_max() == unsorted_list.pop(0)

        check_priority_queue_content(self.under_test, unsorted_list)
