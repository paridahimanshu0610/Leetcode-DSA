from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        dq = deque()
        dq.appendleft((root, (0, 0)))
        res_dict = {}

        while len(dq) != 0:
            node, (r, c) = dq.pop()
            if node.left: dq.appendleft((node.left, (r+1, c-1)))
            if node.right: dq.appendleft((node.right, (r+1, c+1)))

            res_dict[c] = res_dict.get(c, [])
            res_dict[c].append((r, node.val))

        res = []

        for key, val in sorted(res_dict.items(), key = lambda x : x[0]):
            temp = sorted(val, key = lambda x: (x[0], x[1]))
            res.append([val for _, val in temp])

        return res