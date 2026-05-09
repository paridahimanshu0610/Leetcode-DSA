# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDepth(self, root, currDepth):
        if root is None:
            return currDepth-1
        
        return max(self.getDepth(root.left, currDepth+1), self.getDepth(root.right, currDepth+1))
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return self.getDepth(root, 1)    