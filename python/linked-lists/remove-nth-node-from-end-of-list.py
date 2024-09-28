# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr, nxt = None, head, head.next

        while nxt:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = curr.next

        curr.next = prev

        delete = curr
        if n == 1:
            curr = curr.next
        else:
            for i in range(n - 2):
                delete = delete.next

            delete.next = delete.next.next

        head = curr
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