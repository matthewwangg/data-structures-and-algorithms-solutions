# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = defaultdict(int)
        for i, value in enumerate(inorder):
            hashmap[value] = i

        def dfs(remaining):
            if not remaining:
                return

            node = TreeNode(remaining[0])
            left, right = [], []

            for i in remaining[1:]:
                if hashmap[i] > hashmap[node.val]:
                    right.append(i)
                else:
                    left.append(i)

            node.left = dfs(left)
            node.right = dfs(right)
            return node

        return dfs(preorder)

