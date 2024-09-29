# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        nodes = []

        def dfs(node, maximum):
            if not node:
                return

            if node.val >= maximum:
                nodes.append(node.val)

            dfs(node.left, max(maximum, node.val))
            dfs(node.right, max(maximum, node.val))

        dfs(root, root.val)

        return len(nodes)
