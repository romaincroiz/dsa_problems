import pytest

from data_structure.ds_queue import DsQueue


class TestDsQueue:
    def setup_method(self):
        self.under_test = DsQueue()

    def test_should_be_empty(self):
        assert self.under_test.is_empty() == True

    def test_should_not_be_empty_after_enqueue(self):
        self.under_test.enqueue("One")
        assert self.under_test.is_empty() == False

    def test_should_peak_be_none_when_empty(self):
        assert self.under_test.peak() is None

    def test_should_peak_return_front_data(self):
        self.under_test.enqueue("One")
        assert self.under_test.peak() == "One"

    def test_should_peak_return_front_data_when_more_than_one(self):
        self.under_test.enqueue("One")
        self.under_test.enqueue("Two")
        assert self.under_test.peak() == "One"

    def test_should_not_enqueue_none(self):
        with pytest.raises(Exception):
            self.under_test.enqueue(None)

    def test_should_dequeue_fail_if_empty(self):
        with pytest.raises(Exception):
            self.under_test.dequeue()

    def test_should_dequeue_empty_queue_if_one_item(self):
        self.under_test.enqueue("One")
        self.under_test.dequeue()
        assert self.under_test.is_empty() == True
        assert self.under_test.peak() is None

    def test_should_dequeue_remove_and_update_front(self):
        self.under_test.enqueue("One")
        self.under_test.enqueue("Two")
        self.under_test.enqueue("Three")
        assert self.under_test.dequeue() == "One"
        assert self.under_test.peak() == "Two"
        assert self.under_test.dequeue() == "Two"
        assert self.under_test.peak() == "Three"
        assert self.under_test.dequeue() == "Three"
        assert self.under_test.peak() is None
        assert self.under_test.is_empty() == True

    def test_should_print_when_empty(self):
        assert str(self.under_test) == 'None'

    def test_should_print_one_item_queue(self):
        self.under_test.enqueue("item")
        assert str(self.under_test) == "(Front) -> item -> (Back)"

    def test_should_print_values_in_order(self):
        self.under_test.enqueue("1st")
        self.under_test.enqueue("in")
        self.under_test.enqueue("first")
        self.under_test.enqueue("out")
        assert str(self.under_test) == "(Front) -> 1st -> in -> first -> out -> (Back)"
