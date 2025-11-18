from collections import defaultdict, Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 统计次数
        cnt = Counter(tuple(nums))
        elem, freq = cnt.most_common(1)[0]
        return elem