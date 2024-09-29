# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def dfs(node):
            if not node:
                return "N"

            return str(node.val) + " " + dfs(node.left) + " " + dfs(node.right)

        return dfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        processed = data.split(" ")
        if processed[0] == "N":
            return None

        final = TreeNode(int(processed[0]))

        def construct(node, index):
            current = index
            if processed[current] != "N":
                node.left = TreeNode(int(processed[current]))
                current = construct(node.left, current + 1)
            else:
                current += 1

            if processed[current] != "N":
                node.right = TreeNode(int(processed[current]))
                current = construct(node.right, current + 1)
            else:
                current += 1

            return current

        construct(final, 1)
        return final

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))