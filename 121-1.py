from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = max(prices)
        res = 0
        for price in prices:
            if price < min_price:
                min_price = min(price, min_price)
            res = max(res, price - min_price)
        return res
    
if __name__ == '__main__':
    s = Solution()
    # print(s.groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]))
    # lst = ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]
    # default_dict = defaultdict(list)
    # print(default_dict)
    # print(''.join(sorted("scx")))
    print(s.maxProfit([7,1,5,3,6,4]))