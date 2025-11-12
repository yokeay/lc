from collections import defaultdict
from typing import List


class Solution:
    ###
    def longestConsecutive(self, num_list: List[int]) -> int:
        if not num_list:
            return 0
        s_lst= set(num_list)
        mp = {num: Node(num) for num in s_lst}
        max_val = max(num_list)
        min_val = min(num_list)
#       遍历字典中的每一个node，看看nums中是否存在node的前驱或者后继，如果存在，则基于此Node继续寻找
        for num,node in mp.items():
            cur = node
            while cur:
                if cur.get_val() - 1 in s_lst:
                    cur.set_left(mp[cur.get_val() - 1])
                    cur = mp[cur.get_val() - 1]
                    if cur.get_val() == min_val:
                        break
                    continue
                if cur.get_val() + 1 in s_lst:
                    cur.set_right(mp[cur.get_val() + 1])
                    cur = mp[cur.get_val() + 1]
                    if cur.get_val() == max_val:
                        break
                    continue
                break
        max_len = 0
        for node in mp.values():
            max_len = max(max_len, node.get_length())
        return max_len


class Node:
    def __init__(self, val):
        self.val = val
        self.length = 1
        self.left = None
        self.right = None

    def get_val(self):
        return self.val

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def get_length(self):
        # 你可以在需要时计算：从当前向左走到头 + 向右走到头 - 1（因为当前节点算了两次）
        cur = self.left
        left_length = 0
        while cur:
            left_length += 1
            cur = cur.left
        cur = self.right
        right_length = 0
        while cur:
            right_length += 1
            cur = cur.right
        return left_length + 1 + right_length

if __name__ == '__main__':
    nums = [9,1,4,7,3,-1,0,5,8,-1,6]
    solution = Solution()
    res = solution.longestConsecutive(nums)
    # res = solution.longestConsecutive(nums)
    print(res)