from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # 初始化空前缀
        cur_sum = 0
        res = 0

        for num in nums:
            cur_sum += num  # 当前前缀和
            # 关键：看看有没有之前的前缀和让 (cur_sum - prev_sum = k)
            res += prefix_sum_count[cur_sum - k]
            # 更新前缀和出现次数
            prefix_sum_count[cur_sum] += 1

        return res

if __name__ == '__main__':
    nums = [1, 2, 1, 2, 1]
    k = 3
    res = Solution().subarraySum(nums, k)
    print(res)  # ✅ 输出 4
