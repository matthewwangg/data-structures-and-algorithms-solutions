# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestors = []

        def dfs(node):
            hasp, hasq = False, False
            if not node:
                return hasp, hasq

            hasp, hasq = dfs(node.left)
            if hasp:
                _, hasq = dfs(node.right)
            elif hasq:
                hasp, _ = dfs(node.right)
            else:
                hasp, hasq = dfs(node.right)

            if node == p:
                hasp = True
            if node == q:
                hasq = True

            if hasp and hasq:
                ancestors.append(node)

            return hasp, hasq

        dfs(root)
        return ancestors[0]

