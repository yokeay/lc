from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        start_index = 0
        for index in range(len(nums)):
            cur_sum = sum(nums[start_index, index+1])
            if cur_sum < 0:
                start_index = index + 1
            else:
                max_sum = cur_sum
        return max_sum