# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, curr_arr, res):
        if node is None:
            return
        
        curr_arr.append(node.val)
        self.traverse(node.left, curr_arr, res)
        self.traverse(node.right, curr_arr, res)
        
        # If it is a leaf node, then append the curr_arr to res
        if (node.left is None) and (node.right is None):
            res.append("->".join([str(e) for e in curr_arr]))
            
        curr_arr.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res, curr_arr = [], []
        self.traverse(root, curr_arr, res)
        return res