# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast, slow, current = head, head, head
        while fast:
            previousslow = slow
            fast = fast.next
            slow = slow.next
            if fast:
                fast = fast.next

        previousslow.next = None
        tail = []

        def reversal(node):
            if not node.next:
                tail.append(node)
                return node

            nextnode = reversal(node.next)
            nextnode.next = node
            node.next = None

            return node

        if not slow:
            return
        reversal(slow)
        reverse = tail[0]
        while current and reverse:
            temp = current.next
            current.next = reverse
            reverse = reverse.next
            current.next.next = temp
            current = current.next
            current = current.next



