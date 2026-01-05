# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = []
        def mid(node):
            if not node:
                return
            mid(node.left)
            lst.append(node.val)
            mid(node.right)
        mid(root)
        return lst[k-1]