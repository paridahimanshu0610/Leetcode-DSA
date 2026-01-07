# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, node, currDepth):
        if node is None:
            return currDepth-1

        return max(self.getHeight(node.left, currDepth+1), self.getHeight(node.right, currDepth+1))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getHeight(root, 1)