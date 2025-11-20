from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        length = len(nums)
        current_index = 0
        res = []
        while current_index < length:
            current_value = nums[current_index]
            if 1 <= current_value <= length and current_value != nums[current_value-1]:
                nums[current_index], nums[current_value-1] = nums[current_value-1], nums[current_index]
            else:
                current_index += 1
        for index in range(length):
            if nums[index] != index + 1:
                res.append(nums[index])
        return res