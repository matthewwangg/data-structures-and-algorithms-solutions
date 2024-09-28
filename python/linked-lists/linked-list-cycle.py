# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while fast:
            fast = fast.next
            slow = slow.next
            if not fast:
                break
            fast = fast.next
            if fast == slow:
                return True

        return False
