# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []

        def traversal(node):
            if not node:
                return None

            traversal(node.left)
            inorder.append(node.val)
            traversal(node.right)

            return

        traversal(root)
        return inorder

