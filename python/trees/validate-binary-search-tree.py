# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return None, None, True

            leftmin, leftmax, leftvalid = dfs(node.left)
            rightmin, rightmax, rightvalid = dfs(node.right)

            if (leftmin == None or node.val > leftmax) and leftvalid and (
                    rightmax == None or node.val < rightmin) and rightvalid:
                if not leftmin and not rightmax:
                    return node.val, node.val, True
                if not leftmin:
                    return min(node.val, rightmin), max(node.val, rightmax), True
                if not rightmax:
                    return min(node.val, leftmin), max(node.val, leftmax), True

                return min(leftmin, rightmin, node.val), max(leftmax, rightmax, node.val), True

            return 0, 0, False

        _, _, answer = dfs(root)
        return answer