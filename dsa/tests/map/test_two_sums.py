from dsa.solutions.map.two_sums import two_sum


class TestTwoSums:
    """
    Test for two sums

    https://leetcode.com/problems/two-sum/description
    """
    def test_two_sum(self):
        to_test_list = [
            TwoSum([2, 7, 11, 15], 9, [0, 1]),
            TwoSum([3, 2, 4], 6, [1, 2]),
            TwoSum([3,3], 6, [0, 1]),
            TwoSum([1,2], 6, None),
        ]

        for to_test in to_test_list:
            assert_two_sum(to_test)

def assert_two_sum(t: TwoSum):
    actual = two_sum(t.nums, t.target)

    if t.expected is not None:
        assert len(actual) == 2
        # order does not matter
        for i in range(len(t.expected)):
            assert t.expected[i] in actual
    else:
        assert actual is None

class TwoSum:
    def __init__(self, nums: list[int], target: int, expected: list[int] | None):
        self.nums = nums
        self.target = target
        self.expected = expected