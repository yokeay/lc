from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [1] * length
        suffix = [1] * length
        prefix[0] = 1
        suffix[0] = 1
        res = [1] * length
        for index in range(1, length):
            prefix[index] = prefix[index - 1] * nums[index - 1]
        for index in range(length-2, -1, -1):
            suffix[index] = suffix[index + 1] * nums[index + 1]
        for index in range(length):
            res[index] = prefix[index] * suffix[index]
        return res