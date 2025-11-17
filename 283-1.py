from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_index = 0
        right_index = left_index + 1
        for num in nums:
            if nums[left_index] == 0:
                while right_index < len(nums) and nums[right_index] == 0 :
                    right_index += 1
                    continue
                if right_index == len(nums):
                    break
                nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
            left_index += 1
            right_index = max(right_index, left_index + 1)
        return nums



if __name__ == '__main__':
    s = Solution()
    print(s.moveZeroes([0,0]))