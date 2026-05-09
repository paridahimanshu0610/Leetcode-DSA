# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, res):
        if root is None:
            return res

        res.append(root.val)
        self.traverse(root.left, res)
        self.traverse(root.right, res)

        return res
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traverse(root, [])