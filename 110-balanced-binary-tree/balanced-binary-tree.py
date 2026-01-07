# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeightAndBalance(self, node, currHeight):
        if node is None:
            return (currHeight, True)

        leftHeight, isLeftBalanced = self.getHeightAndBalance(node.left, currHeight)
        rightHeight, isRightBalanced = self.getHeightAndBalance(node.right, currHeight)

        isTreeBalanced = (abs(leftHeight-rightHeight)<=1) and isLeftBalanced and isRightBalanced

        return max(leftHeight, rightHeight)+1, isTreeBalanced

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height, isBalanced = self.getHeightAndBalance(root, -1)
        return isBalanced 