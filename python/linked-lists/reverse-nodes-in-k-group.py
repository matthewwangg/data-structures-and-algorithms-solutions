# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        count = 1
        groups = [head]
        while current:
            nxt = current.next
            if count % k == 0:
                current.next = None
                groups.append(nxt)
                count = 0
            current = nxt
            count += 1

        def reversal(node):
            if not node:
                return node
            prev, curr, nxt = None, node, node.next

            while nxt:
                curr.next = prev
                prev = curr
                curr = nxt
                nxt = curr.next

            curr.next = prev

            return curr

        finalanswer = ListNode(0)
        final = finalanswer
        for i in groups[:-1]:
            rev = reversal(i)
            final.next = rev
            while final.next:
                final = final.next

        last = groups[-1]
        counter = 0
        while last:
            counter += 1
            last = last.next

        if counter != k:
            final.next = groups[-1]
        else:
            final.next = reversal(groups[-1])
        return finalanswer.next