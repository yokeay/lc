# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            # 更新最长路径（通过此节点）
            self.ans = max(self.ans, left + right)
            # 返回当前节点的深度
            return max(left, right) + 1
        depth(root)
        return self.ans