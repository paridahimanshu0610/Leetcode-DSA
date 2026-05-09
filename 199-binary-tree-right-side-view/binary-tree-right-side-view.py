# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        dq = deque()
        dq.appendleft((root, (0, 0)))
        res = []

        while len(dq) != 0:
            rightmost_idx = -float('inf')
            rightmost_val = None
            curr_size = len(dq)
            
            for i in range(curr_size):
                node, (r, c) = dq.pop()
                if i==0:
                    res.append(node.val)
                
                if node.right: dq.appendleft((node.right, (r+1, c+1)))
                if node.left: dq.appendleft((node.left, (r+1, c-1)))

        return res