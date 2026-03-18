def two_sum(nums: list[int], target: int) -> list[int] | None:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    https://leetcode.com/problems/two-sum/description

    - Each input have exactly one solution
    - Can return the answer in any order
    """
    map_counterpart = {}

    for ind, num in enumerate(nums):
        counterpart = target - num
        if counterpart not in map_counterpart:
            map_counterpart[num] = ind
        else:
            return [ind, map_counterpart[counterpart]]
    return None