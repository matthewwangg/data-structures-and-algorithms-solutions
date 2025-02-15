# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        def replacement(node, direction):
            if direction == "left":
                node = node.left
                while node.right:
                    node = node.right
            else:
                node = node.right
                while node.left:
                    node = node.left

            return node.val

        if key == root.val:
            if not root.left and not root.right:
                return None
            elif not root.right:
                root.val = replacement(root, "left")
                root.left = self.deleteNode(root.left, root.val)
            else:
                root.val = replacement(root, "right")
                root.right = self.deleteNode(root.right, root.val)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root


