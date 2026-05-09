# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, res):
        if root is None:
            return (0, res)

        left, res = self.dfs(root.left, res)
        right, res = self.dfs(root.right, res)

        depth = 1 + max(left, right)

        return (depth, max(res, left+right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, diameter = self.dfs(root, -1)

        return diameter