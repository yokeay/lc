from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        left_sum = 0
        total = sum(nums)
        
        # 如果总和是奇数，直接返回 0
        if total % 2 != 0:
            return 0

        for index in range(n - 1):  # 遍历到倒数第二个元素，确保右侧不为空
            left_sum += nums[index]
            # 判断 left_sum 的两倍与总和的差是否为偶数
            if (total - 2 * left_sum) % 2 == 0:
                count += 1

        return count
