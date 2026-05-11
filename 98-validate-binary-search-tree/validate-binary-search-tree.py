# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inRange(self, node, lower, upper):
        if node is None:
            return True

        return (lower < node.val < upper) and self.inRange(node.left, lower, node.val) and self.inRange(node.right, node.val, upper)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.inRange(root, float("-inf"), float("inf"))