# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        newNode = TreeNode(val)

        if root is None:
            return newNode
        while node:
            if node.val > val:
                if node.left:
                    node = node.left
                else:
                    node.left = newNode
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = newNode
                    break

        return root