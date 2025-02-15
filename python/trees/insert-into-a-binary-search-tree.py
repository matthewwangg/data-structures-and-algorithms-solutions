# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def find(node):
            if not node:
                return TreeNode(val)

            if node.val < val:
                node.right = find(node.right)
            else:
                node.left = find(node.left)

            return node

        root = find(root)

        return root
