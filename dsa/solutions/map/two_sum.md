# Two Sum

## Problem
- array of integers > `nums`
- integer > `target`
- return indices of the two numbers such that they add up to `target`.

Exactly one solution
May not use the same element twice
Return the answer in any order.

## Examples

### Example 1

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

### Example 2

Input: nums = [3,2,4], target = 6
Output: [1,2]

### Example 3

Input: nums = [3,3], target = 6
Output: [0,1]

## Constraints

- 2 <= nums.length <= 104
- -109 <= nums[i] <= 109
- -109 <= target <= 109
- Only one valid answer exists.
 
## Follow-Up

Can you come up with an algorithm that is less than O(n2) time complexity?


## Intuition

To find the sum: for each `elt`, find `elt2` so that all are true:
- `target - elt = elt2`
- `elt != elt2`

### Naive solution: Brute force O(n2)

- 2 loops to find the pair that adds up to target
- Time complexity is O(n2) because for each elt we have an inner loop (n iteration)

for each elt in nums:
    for each elt2 in nums:
        if elt != elt2 && target - elt == elt2
            return [elt, elt2]
return

### Naive solution: Brute force O(n)

- one loop, store elt + index in hashmap as they are visited
- for each elt, check if target - elt is in the map -> return the indexes
- Time complexity is O(n) because each value is visited at most once