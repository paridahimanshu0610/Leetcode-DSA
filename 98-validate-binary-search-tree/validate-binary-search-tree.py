# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, arr):
        if root is None:
            return

        self.traverse(root.left, arr)
        arr.append(root.val)
        self.traverse(root.right, arr)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        self.traverse(root, arr)

        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                return False

        return True