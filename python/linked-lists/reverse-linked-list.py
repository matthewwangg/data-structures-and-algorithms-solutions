# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        prev, curr, nxt = None, head, head.next

        while nxt:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = curr.next

        curr.next = prev

        return curr