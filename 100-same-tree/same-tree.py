from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        dq = deque()

        if (not p and q) or (p and not q):
            return False
        
        if not p and not q:
            return True

        dq.appendleft((p, q))

        while len(dq)!=0:
            t1, t2 = dq.pop()
            if t1.val != t2.val:
                return False

            if (t1.left and not t2.left) or (not t1.left and t2.left) or (t1.right and not t2.right) or (not t1.right and t2.right):
                return False            
            if t1.left and t2.left:
                dq.appendleft((t1.left, t2.left))
            if t1.right and t2.right:
                dq.appendleft((t1.right, t2.right))

        return True

