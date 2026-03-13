import pytest

from data_structure.ds_dynamic_array import DsDynamicArray


class TestDsDynamicArray:

    def setup_method(self):
        self.under_test = DsDynamicArray()

    def test_should_init_with_invalid_size(self):
        self.under_test = DsDynamicArray(-1)

    def test_should_be_empty(self):
        assert len(self.under_test) == 0

    def test_should_not_insert_negative_index(self):
        with pytest.raises(IndexError):
            self.under_test.insert(-1, "inserted out of bounds")

    def test_should_not_insert_out_of_bounds(self):
        with pytest.raises(IndexError):
            self.under_test.insert(1, "inserted out of bounds")

    def test_should_not_insert_out_of_bounds_when_one_element(self):
        self.under_test.insert(0, "can be inserted")
        with pytest.raises(IndexError):
            self.under_test.insert(2, "inserted out of bounds")

    def test_should_insert_at_index(self):
        self.under_test.insert(0, "can be inserted")
        assert len(self.under_test) == 1
        assert self.under_test.get(0) == "can be inserted"

    def test_should_insert_none_at_index(self):
        self.under_test.insert(0, None)
        assert len(self.under_test) == 1
        assert self.under_test.get(0) is None

    def test_should_append_none(self):
        self.under_test.append(None)
        assert len(self.under_test) == 1
        assert self.under_test.get(0) is None

    def test_should_clear_if_empty(self):
        self.under_test.clear()
        assert len(self.under_test) == 0

    def test_should_clear_if_not_empty(self):
        self.under_test.append(0)
        self.under_test.append(1)
        self.under_test.clear()
        assert len(self.under_test) == 0

    def test_should_not_get_negative_index(self):
        with pytest.raises(IndexError):
            self.under_test.get(-1)

    def test_should_not_get_out_of_bounds(self):
        with pytest.raises(IndexError):
            assert self.under_test.get(0)

    def test_should_get_first_value(self):
        self.under_test.append("first")
        self.under_test.append("second")
        assert self.under_test.get(0) == "first"

    def test_should_get_last_value(self):
        self.under_test.append("first")
        self.under_test.insert(1,"last")
        assert self.under_test.get(1) == "last"

    def test_should_get_middle_value(self):
        self.under_test.append("first")
        self.under_test.append("last")
        self.under_test.insert(1,"middle")
        assert self.under_test.get(1) == "middle"

    def test_should_print_when_empty(self):
        assert str(self.under_test) == "[]"

    def test_should_print_when_contains_none_values(self):
        self.under_test.append(1)
        self.under_test.append(None)
        assert str(self.under_test) == "[1, None]"

    def test_should_print_values_in_order(self):
        self.under_test.append("first")
        self.under_test.append("last")
        self.under_test.insert(1, "middle")
        assert str(self.under_test) == "[first, middle, last]"

    def test_should_not_remove_negative_index(self):
        with pytest.raises(IndexError):
            self.under_test.remove(-1)

    def test_should_not_remove_out_of_bounds(self):
        self.under_test.append("first")
        self.under_test.append("last")
        with pytest.raises(IndexError):
            assert self.under_test.remove(2)

    def test_should_not_remove_if_empty(self):
        with pytest.raises(IndexError):
            assert self.under_test.remove(0)

    def test_should_remove_first(self):
        self.under_test.append("first")
        self.under_test.append("last")
        assert self.under_test.remove(0)
        assert len(self.under_test) == 1
        assert self.under_test.get(0) == "last"

    def test_should_remove_last(self):
        self.under_test.append("first")
        self.under_test.append("middle")
        self.under_test.append("last")
        assert self.under_test.remove(2)
        assert len(self.under_test) == 2
        assert self.under_test.get(0) == "first"
        assert self.under_test.get(1) == "middle"

    def test_should_remove_middle(self):
        self.under_test.append("first")
        self.under_test.append("middle")
        self.under_test.append("last")
        assert self.under_test.remove(1)
        assert len(self.under_test) == 2
        assert self.under_test.get(0) == "first"
        assert self.under_test.get(1) == "last"