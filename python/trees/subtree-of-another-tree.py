# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        candidates = []

        def checker(node):
            if not node:
                return

            if node.val == subRoot.val:
                candidates.append(node)

            checker(node.left)
            checker(node.right)

        checker(root)

        def dfs(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return dfs(p.left, q.left) and dfs(p.right, q.right)

        for i in candidates:
            if dfs(i, subRoot):
                return True

        return False
