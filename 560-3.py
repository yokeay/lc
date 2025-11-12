from collections import defaultdict
from typing import List


#  和为 K 的子数组
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, prefix, res = defaultdict(int, {0:1}), 0, 0
        for num in nums:
            prefix += num
            res += count[prefix-k]
            count[prefix] += 1
        return res

if __name__ == '__main__':
    nums = [1,1,1]
    k = 2
    res = Solution().subarraySum(nums, k)
    print(res)

