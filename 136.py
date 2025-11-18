from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        least_elem = min(cnt, key=cnt.get)
        print(least_elem)  # 1