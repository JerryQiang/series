"""
难度: Easy
原题链接:https://leetcode.com/problems/two-sum

内容描述:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

from typing import List

class Solution(object):
    def twoSumV1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSumV2(self, nums: List[int], target: int) -> List[int]:
        loop = {}
        for i in range(len(nums)):
            res = target-nums[i]
            if res in loop:
                return [loop[res], i]
            else:
                loop[nums[i]] = i




if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    print(solution.twoSumV1(nums, target))
    print(solution.twoSumV2(nums, target))