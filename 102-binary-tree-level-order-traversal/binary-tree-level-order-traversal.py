from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        temp = deque()
        temp.appendleft((1, root))
        res = []

        while len(temp)!=0:
            level, node = temp.pop()
            if node.left: temp.appendleft((level+1, node.left))
            if node.right: temp.appendleft((level+1, node.right))

            if len(res) <  level:
                res.append([node.val])
            else:
                res[level-1].append(node.val)

        return res