# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.prev = None    # ← 原来的 head，语义修正

        def pre(node):
            if not node:
                return

            # 🔑 先保存
            left = node.left
            right = node.right

            # 🔧 用 prev 串原树节点
            if self.prev:
                self.prev.left = None
                self.prev.right = node

            # 更新 prev
            self.prev = node

            pre(left)
            pre(right)

        pre(root)
