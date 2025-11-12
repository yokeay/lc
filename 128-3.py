from typing import List

class Solution:
    def longestConsecutive(self, num_list: List[int]) -> int:
        if not num_list:
            return 0

        s = set(num_list)
        mp = {num: Node(num) for num in s}

        # 建立左右关系
        for num, node in mp.items():
            if num - 1 in mp:
                node.set_left(mp[num - 1])
            if num + 1 in mp:
                node.set_right(mp[num + 1])

        # 只从左端点向右遍历
        max_len = 0
        for node in mp.values():
            if node.left is None:
                cur = node
                length = 0
                while cur:
                    length += 1
                    cur = cur.right
                max_len = max(max_len, length)

        return max_len


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def get_val(self):
        return self.val

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

if __name__ == '__main__':
    nums = [9,1,4,7,3,-1,0,5,8,-1,6]
    solution = Solution()
    print(solution.longestConsecutive(nums))  # ✅ 输出 7
