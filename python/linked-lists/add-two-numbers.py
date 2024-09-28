# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        current = head
        carry = 0
        while l1 or l2 or carry:
            if l1 and l2:
                sum = carry + l1.val + l2.val
                carry = sum // 10
                current.next = ListNode(sum % 10)
                l1 = l1.next
                l2 = l2.next
            else:
                if l1:
                    sum = carry + l1.val
                    carry = sum // 10
                    current.next = ListNode(sum % 10)
                    l1 = l1.next
                elif l2:
                    sum = carry + l2.val
                    carry = sum // 10
                    current.next = ListNode(sum % 10)
                    l2 = l2.next
                else:
                    current.next = ListNode(carry)
                    carry = 0
            current = current.next

        return head.next
