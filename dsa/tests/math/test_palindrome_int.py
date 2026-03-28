from dsa.solutions.math.palindrome_int import is_palindrome_int


class TestPalindromeInt:
    """
        Test for integer palindrome

        LeetCode: https://leetcode.com/problems/palindrome-number/description
        """

    def test_negative_not_valid(self):
        assert is_palindrome_int(-120) == False

    def test_ten_one_digit_valid(self):
        assert is_palindrome_int(0) == True
        assert is_palindrome_int(1) == True
        assert is_palindrome_int(2) == True
        assert is_palindrome_int(3) == True
        assert is_palindrome_int(4) == True
        assert is_palindrome_int(5) == True
        assert is_palindrome_int(6) == True
        assert is_palindrome_int(7) == True
        assert is_palindrome_int(8) == True
        assert is_palindrome_int(9) == True

    def test_ten_multiples_not_valid(self):
        assert is_palindrome_int(10) == False
        assert is_palindrome_int(100) == False
        assert is_palindrome_int(1000) == False
        assert is_palindrome_int(10000) == False

    def test_odd_digits_are_handled(self):
        assert is_palindrome_int(121) == True
        assert is_palindrome_int(122) == False
        assert is_palindrome_int(221) == False
        assert is_palindrome_int(12221) == True

    def test_even_digits_are_handled(self):
        assert is_palindrome_int(11) == True
        assert is_palindrome_int(12) == False
        assert is_palindrome_int(1221) == True
        assert is_palindrome_int(1121) == False
        assert is_palindrome_int(112211) == True
        assert is_palindrome_int(122211) == False