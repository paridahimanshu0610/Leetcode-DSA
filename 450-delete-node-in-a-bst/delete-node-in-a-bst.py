# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getRightMostNode(self, node):
        while node and node.right:
            node = node.right
        return node

    def shuffle(self, node):
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            rightmostNode = self.getRightMostNode(node.left)
            rightmostNode.right = node.right
            node.right = None
            return node.left

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if root.val == key:
            return self.shuffle(root)

        node = root
        while node:
            leftPtr, rightPtr = node.left, node.right

            if leftPtr and leftPtr.val==key:
                node.left = self.shuffle(leftPtr)
            elif rightPtr and rightPtr.val==key:
                node.right = self.shuffle(rightPtr)
            
            if node.val > key:
                node = node.left
            else:
                node = node.right

        return root