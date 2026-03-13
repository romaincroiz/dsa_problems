import pytest

from data_structure.ds_linked_list import DsLinkedList


class TestDsLinkedList:
    def setup_method(self):
        self.under_test = DsLinkedList()

    def test_should_be_empty(self):
        assert len(self.under_test) == 0
        assert self.under_test.is_empty()

    def test_should_not_be_empty_after_adding(self):
        self.under_test.add(0, "first")
        assert len(self.under_test) == 1
        assert self.under_test.is_empty() == False

    def test_should_not_add_negative_index(self):
        with pytest.raises(IndexError):
            self.under_test.add(-1, "added out of bounds")

    def test_should_not_add_out_of_bounds(self):
        with pytest.raises(IndexError):
            self.under_test.add(1, "added out of bounds")

    def test_should_not_add_out_of_bounds_when_one_element(self):
        self.under_test.add(0, "can be add")
        with pytest.raises(IndexError):
            self.under_test.add(2, "added out of bounds")

    def test_should_add_at_index(self):
        self.under_test.add(0, "can be add")
        assert len(self.under_test) == 1
        assert self.under_test.get(0) == "can be add"

    def test_should_not_add_none_at_index(self):
        with pytest.raises(Exception):
            self.under_test.add(0, None)

    def test_should_add_at_head_when_not_empty(self):
        self.under_test.add(0, "previous head")
        self.under_test.add(0, "new head")
        assert len(self.under_test) == 2
        assert self.under_test.get(0) == "new head"

    def test_should_add_at_tail(self):
        self.under_test.add(0, "previous tail")
        self.under_test.add(1, "new tail")
        assert len(self.under_test) == 2
        assert self.under_test.get(1) == "new tail"

    def test_should_add_in_middle(self):
        self.under_test.add(0, "tail")
        self.under_test.add(0, "head")
        self.under_test.add(1, "middle")
        assert len(self.under_test) == 3
        assert self.under_test.get(0) == "head"
        assert self.under_test.get(2) == "tail"
        assert self.under_test.get(1) == "middle"

    def test_should_clear_if_empty(self):
        self.under_test.clear()
        assert len(self.under_test) == 0

    def test_should_clear_if_not_empty(self):
        self.under_test.add(0, 1)
        self.under_test.add(0, 0)
        self.under_test.clear()
        assert len(self.under_test) == 0
        assert self.under_test.is_empty()

    def test_should_peak_if_empty(self):
        assert self.under_test.peak() is None

    def test_should_peak_if_not_empty(self):
        self.under_test.add(0, "tail")
        self.under_test.add(0, "head")
        assert self.under_test.peak() == "head"

    def test_should_not_get_negative_index(self):
        with pytest.raises(IndexError):
            self.under_test.get(-1)

    def test_should_not_get_out_of_bounds(self):
        with pytest.raises(IndexError):
            assert self.under_test.get(0)

    def test_should_get_first_value(self):
        self.under_test.add(0, "tail")
        self.under_test.add(0, "head")
        assert self.under_test.get(0) == "head"

    def test_should_get_last_value(self):
        self.under_test.add(0, "tail")
        self.under_test.add(0, "head")
        self.under_test.add(1, "middle")
        assert self.under_test.get(2) == "tail"

    def test_should_get_middle_value(self):
        self.under_test.add(0, "tail")
        self.under_test.add(0, "head")
        self.under_test.add(1, "middle")
        assert self.under_test.get(1) == "middle"

    def test_should_print_when_empty(self):
        assert str(self.under_test) == 'None'

    def test_should_print_values_in_order(self):
        self.under_test.add(0, "tail")
        self.under_test.add(0, "head")
        self.under_test.add(1, "middle")
        assert str(self.under_test) == "head -> middle -> tail"

    def test_should_not_remove_first_if_empty(self):
        with pytest.raises(Exception):
            self.under_test.remove_first("head")

    def test_should_not_remove_first_none_value(self):
        with pytest.raises(Exception):
            self.under_test.remove_first(None)

    def test_should_return_false_when_remove_first_not_found(self):
        self.under_test.add(0, "tail")
        self.under_test.add(0, "head")
        self.under_test.add(0, "middle")
        assert self.under_test.remove_first("not found") == False

    def test_should_remove_first_remove_head_if_first_found(self):
        self.under_test.add(0, "bar")
        assert self.under_test.remove_first("bar")
        assert len(self.under_test) == 0

    def test_should_remove_first_if_found(self):
        self.under_test.add(0, "bar")
        self.under_test.add(0, "foo")
        self.under_test.add(0, "bar")
        self.under_test.add(0, "foo")
        assert self.under_test.remove_first("bar")
        assert len(self.under_test) == 3
        assert self.under_test.get(0) == "foo"
        assert self.under_test.get(1) == "foo"
        assert self.under_test.get(2) == "bar"

    def test_should_not_remove_negative_index(self):
        self.under_test.add(0, "head")
        with pytest.raises(IndexError):
            self.under_test.remove_at(-1)

    def test_should_not_remove_out_of_bounds(self):
        self.under_test.add(0, "tail")
        self.under_test.add(0, "head")
        with pytest.raises(IndexError):
            assert self.under_test.remove_at(2)

    def test_should_not_remove_if_empty(self):
        with pytest.raises(Exception):
            assert self.under_test.remove_at(0)

    def test_should_remove_first(self):
        self.under_test.add(0, "tail")
        self.under_test.add(0, "head")
        assert self.under_test.remove_at(0)
        assert len(self.under_test) == 1
        assert self.under_test.get(0) == "tail"

    def test_should_remove_last(self):
        self.under_test.add(0, "tail")
        self.under_test.add(0, "middle")
        self.under_test.add(0, "head")
        assert self.under_test.remove_at(2)
        assert len(self.under_test) == 2
        assert self.under_test.peak() == "head"
        assert self.under_test.get(1) == "middle"

    def test_should_remove_middle(self):
        self.under_test.add(0, "tail")
        self.under_test.add(0, "middle")
        self.under_test.add(0, "head")
        assert self.under_test.remove_at(1)
        assert len(self.under_test) == 2
        assert self.under_test.peak() == "head"
        assert self.under_test.get(1) == "tail"
