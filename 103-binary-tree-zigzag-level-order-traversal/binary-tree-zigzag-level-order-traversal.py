from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque()

        if root is None:
            return []

        res = []
        order = 1
        dq.append(root)

        while len(dq) != 0:
            curr_size = len(dq)
            temp = [None]*curr_size

            for i in range(curr_size):
                node = dq.pop()
                if node.left: dq.appendleft(node.left)
                if node.right: dq.appendleft(node.right)
                
                idx = curr_size-1-i if order < 0 else i
                temp[idx] = node.val

            order *= -1
            res.append(temp)

        return res