# Palindrome

## Problem

A phrase is a palindrome if after converting all uppercase letters into lowercase letters and removing all non-alphanumeric 
characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Examples

### Example 1

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

### Example 2

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

### Example 3

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

## Constraints

- 1 <= s.length <= 2 * 105
- s consists only of printable ASCII characters.
 

## Intuition

- convert into lowercase letters
- remove all non-alphanumeric
- it reads the same forward and backward → symetry from the middle


### Naive solution: Time O(n), Space O(n)

1. Cleaning the string first → Time O(n), Space O(n)
```python
cleaned_string = "".join(char.lower() for char in s if char.isalnum())
```
2. Reverse it → Time O(n), Space O(n)

Using slicing in Python

```python
# string[start:stop:step]
# so here we explore the entire string moving backwards, which reverse it 
reversed_string = cleaned_string[::-1]
```

3. Check if it looks exactly the same as s: Time O(n)

### Optimized solution: Two pointers → Time O(n), Space O(1)

- Explore with two pointers, one from each end until they meet
- Ignore non-alpha and lowercase as we explore to avoid another pass

