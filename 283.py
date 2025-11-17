from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_index = 0
        right_index = len(nums)-1
        for num in nums:
            if nums[left_index] == 0 and left_index < right_index:
                while nums[right_index] == 0 and left_index < right_index:
                    right_index += 1
                    continue
                nums[left_index] = nums[right_index]
                nums[right_index] = 0
                left_index += 1
                right_index += 1
                continue
            left_index += 1
        return nums

if __name__ == '__main__':
    s = Solution()
    print(s.moveZeroes([0,1,0,3,12]))