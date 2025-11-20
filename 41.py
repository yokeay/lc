from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        current_index = 0
        while current_index < length:
            current_value = nums[current_index]
            if 1<= current_value <= length and current_index != current_value -1 and current_value != nums[current_value-1]:
                cache_value = nums[current_value-1]
                nums[current_value-1] = current_value
                nums[current_index] = cache_value
            else:
                current_index += 1
        for index in range(len(nums)):
            if nums[index] != index + 1:
                return index + 1
        return length + 1       
 