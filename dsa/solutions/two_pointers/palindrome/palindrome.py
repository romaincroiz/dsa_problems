def is_palindrome_brute(s:str) -> bool:
    # 1. Cleaning the string first
    cleaned_string = "".join(char.lower() for char in s if char.isalnum())
    # 2. Reverse it
    reversed_string = cleaned_string[::-1]
    # 3. Check if it looks exactly the same as s
    return cleaned_string == reversed_string


def is_palindrome(s:str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


def test_is_palindrome():
    assert_is_palindrome('A man, a plan, a canal: Panama', True)
    assert_is_palindrome('race a car', False)
    assert_is_palindrome(' ', True)
    assert_is_palindrome('aa,', True)
    assert_is_palindrome('', True)
    assert_is_palindrome(', ', True)


def assert_is_palindrome(s, expected):
    assert is_palindrome(s) == expected