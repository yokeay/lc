from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = 0
        if len(nums) < 3:
            return []
        nums.sort()
        for i in range(len(nums)):
            left_index = i+1
            right_index = len(nums)-1
            while left_index < right_index:
