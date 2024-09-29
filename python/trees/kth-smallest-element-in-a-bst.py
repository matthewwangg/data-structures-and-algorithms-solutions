# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = []

        def inorder(node):
            if not node:
                return

            left = inorder(node.left)
            if left:
                array.append(left.val)
            array.append(node.val)
            right = inorder(node.right)
            if right:
                array.append(right.val)

            return

        inorder(root)
        return array[k - 1]
