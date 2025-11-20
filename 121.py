from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right_index = int((len(prices) - 1)/2)
        left_index = right_index
        res = 0
        min_value = prices[left_index]
        max_value = 0
        while left_index >= 0 and right_index < len(prices):
            if prices[left_index] <= min_value:
                res = max((prices[right_index] - prices[left_index]), res)
                left_index -= 1
            if prices[right_index] >= max_value:
                res = max((prices[right_index] - prices[left_index]), res)
                right_index += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1]))