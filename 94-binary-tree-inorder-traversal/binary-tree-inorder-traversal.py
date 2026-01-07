# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node, curr_list):
        if node is None:
            return curr_list
        
        curr_list = self.inorder(node.left, curr_list)
        curr_list.append(node.val)
        curr_list = self.inorder(node.right, curr_list)

        return curr_list

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorder(root, [])