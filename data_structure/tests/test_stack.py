import pytest

from data_structure.ds_stack import DsStack


class TestDsStack:
    def setup_method(self):
        self.under_test = DsStack()

    def test_should_be_empty(self):
        assert self.under_test.is_empty()

    def test_should_not_be_empty_after_adding(self):
        self.under_test.push("first")
        assert self.under_test.is_empty() == False

    def test_should_not_push_none(self):
        with pytest.raises(Exception):
            self.under_test.push(None)

    def test_should_push_on_top_when_empty(self):
        self.under_test.push("first")
        assert self.under_test.is_empty() == False
        assert self.under_test.peak() == "first"

    def test_should_push_on_top_when_not_empty(self):
        self.under_test.push("first")
        self.under_test.push("second")
        assert self.under_test.is_empty() == False
        assert self.under_test.peak() == "second"

    def test_should_clear_if_empty(self):
        self.under_test.clear()
        assert self.under_test.is_empty()

    def test_should_clear_if_not_empty(self):
        self.under_test.push("first")
        self.under_test.push("second")
        self.under_test.clear()
        assert self.under_test.is_empty()

    def test_should_peak_if_empty(self):
        assert self.under_test.peak() is None

    def test_should_peak_if_not_empty(self):
        self.under_test.push("first")
        self.under_test.push("second")
        assert self.under_test.peak() == "second"

    def test_should_not_pop_if_empty(self):
        with pytest.raises(Exception):
            self.under_test.pop()

    def test_should_pop_last_added_value(self):
        self.under_test.push(1)
        self.under_test.push(2)
        self.under_test.push(3)
        assert self.under_test.pop() == 3
        assert self.under_test.is_empty() == False

    def test_should_pop_top_value(self):
        self.under_test.push("last")
        assert self.under_test.pop() == "last"
        assert self.under_test.is_empty() == True

    def test_should_print_when_empty(self):
        assert str(self.under_test) == 'None'

    def test_should_print_values_in_order(self):
        self.under_test.push("first")
        self.under_test.push("in")
        self.under_test.push("last")
        self.under_test.push("out")
        assert str(self.under_test) == "(Top) -> out -> last -> in -> first"