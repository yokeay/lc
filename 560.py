from collections import defaultdict
from typing import List


#  和为 K 的子数组
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        couple_cnt = 0
        for index, value in enumerate(nums):
            left_index = index
            right_index = index + 1
            while right_index < len(nums):
                if nums[left_index] == k or nums[right_index] == k:
                    couple_cnt += 1
                    left_index += 1
                    right_index += 1
                    continue
                if nums[left_index] + nums[right_index] == k:
                    couple_cnt += 1
                    left_index += 1
                    right_index += 1
                    continue
        return couple_cnt

if __name__ == '__main__':
    nums = [1,1,1]
    k = 2
    res = Solution().subarraySum(nums, k)
    print(res)

