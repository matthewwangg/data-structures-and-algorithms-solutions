# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answers = []

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            answers.append(max(left + node.val, right + node.val, node.val, left + right + node.val))

            return max(left + node.val, right + node.val, node.val)

        dfs(root)

        return max(answers)


