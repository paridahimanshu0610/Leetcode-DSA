# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getPath(self, node, target, path):
        if node is None:
            return False

        path.append(node)
        if node == target:
            return True
        
        if self.getPath(node.left, target, path) or self.getPath(node.right, target, path):
            return True
        
        path.pop()

        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1, path2 = [], []
        self.getPath(root, p, path1)
        self.getPath(root, q, path2)

        res = root
        i, j = 1, 1

        while i < len(path1) and j < len(path2):
            if path1[i] == path2[j]:
                res = path1[i]
                i += 1
                j += 1
            else:
                break

        return res