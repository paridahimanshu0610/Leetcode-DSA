# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinVal(self, root):
        if root is None:
            return float('inf')

        res = root.val
        while root.left:
            root = root.left
            res = root.val
        
        return res

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                minVal = self.findMinVal(root.right)
                root.val = minVal
                root.right = self.deleteNode(root.right, minVal)
                return root

        return root
            
