# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        finalanswer = []
        q = deque()
        q.append((root, 0))
        while q:
            current = q.popleft()
            if current[0]:
                if len(finalanswer) <= current[1]:
                    finalanswer.append([])
                finalanswer[current[1]].append(current[0].val)
                q.append((current[0].left, current[1] + 1))
                q.append((current[0].right, current[1] + 1))

        return finalanswer
