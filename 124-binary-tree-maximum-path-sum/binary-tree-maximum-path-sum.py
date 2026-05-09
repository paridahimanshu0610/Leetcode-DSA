# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        res = -float('inf')

        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            nonlocal res
            left = left if left > 0 else 0
            right = right if right > 0 else 0
            
            res = max(res, node.val + left + right)

            return node.val + max(left, right)

        dfs(root)

        return res  

        