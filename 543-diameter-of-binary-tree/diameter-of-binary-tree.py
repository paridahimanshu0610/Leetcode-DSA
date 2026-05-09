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

        left_dia = left if left-1 >= 0 else left
        right_dia = right if right-1 >= 0 else right

        return (depth, max(res, left_dia+right_dia))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, diameter = self.dfs(root, -1)

        return diameter