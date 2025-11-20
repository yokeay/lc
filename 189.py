from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        new_lst = [0] * length
        for index in range(length):
            new_lst[(index + k) % length] = nums[index]
        nums[:] = new_lst
        return nums