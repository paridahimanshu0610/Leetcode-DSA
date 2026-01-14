# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def in_order_traversal(self, node, k, curr_at, curr_val):
        if (node is None) or (curr_at==k):
            return (curr_at, curr_val)
        
        (curr_at, curr_val) = self.in_order_traversal(node.left, k, curr_at, curr_val)
        # print("after left", node.val, curr_at, curr_val)
        
        if curr_at!=k:
            curr_at += 1
            curr_val = node.val
        else:
            return (curr_at, curr_val) 
        # print("after update", node.val, curr_at, curr_val)
        
        (curr_at, curr_val) = self.in_order_traversal(node.right, k, curr_at, curr_val)
        # print("after right", node.val, curr_at, curr_val)

        return (curr_at, curr_val)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        (_, curr_val) = self.in_order_traversal(root, k, 0, None)
        return curr_val