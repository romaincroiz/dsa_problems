from dsa.solutions.two_pointers.palindrome.palindrome import is_palindrome

class TestPalindrome:
    """
    Test for Palindrome problem

    https://leetcode.com/problems/valid-palindrome/description/
    """

    def __init__(self, s: str, expected: bool):
        self.s = s
        self.expected = expected

def test_palindrome():
    to_test_list = [
        TestPalindrome('A man, a plan, a canal: Panama', True),
        TestPalindrome('race a car', False),
        TestPalindrome(' ', True),
        TestPalindrome('aa,', True),
        TestPalindrome('', True),
        TestPalindrome(', ', True),
    ]

    for to_test in to_test_list:
        assert is_palindrome(to_test.s) == to_test.expected