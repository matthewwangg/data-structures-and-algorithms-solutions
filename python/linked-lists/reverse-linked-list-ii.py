# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        newhead = ListNode(0, head)
        end = newhead
        for i in range(left - 1):
            end = end.next

        flip = end.next
        curr = end.next
        end.next = None

        for i in range(right - left):
            if not curr:
                break
            curr = curr.next

        last = curr.next
        curr.next = None
        flip = self.reverse(flip)

        end.next = flip
        while end.next:
            end = end.next
        end.next = last
        return newhead.next

    def reverse(self, node):
        if not node or not node.next:
            return node

        p, c, n = node, node.next, node.next.next
        node.next = None
        while c:
            c.next = p
            p = c
            c = n
            if n:
                n = n.next

        return p

    