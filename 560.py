from collections import defaultdict
from typing import List


#  和为 K 的子数组
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        cnt = 0
        mp = {0: 1}  # 前缀和为0出现1次，用于从开头开始的子数组

        for num in nums:
            prefix += num
            # 查找是否存在前缀和为 prefix - k
            if prefix - k in mp:
                cnt += mp[prefix - k]
            # 把当前前缀和加入计数
            mp[prefix] = mp.get(prefix, 0) + 1

        return cnt

if __name__ == '__main__':
    nums = [1,1,1]
    k = 2
    res = Solution().subarraySum(nums, k)
    print(res)

