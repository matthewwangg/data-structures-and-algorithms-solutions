# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            if not node:
                return 0, 0

            prevl, prevprevl = traverse(node.left)
            prevr, prevprevr = traverse(node.right)

            curr = max(prevprevl + prevprevr + node.val, prevl + prevr)

            return curr, prevl + prevr

        maximum, _ = traverse(root)

        return maximum
