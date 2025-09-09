# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if a % b == 0:
                return b
            
            return gcd(b, a % b)

        left, right = head, head.next

        while right:
            a, b = left.val, right.val
            if b > a:
                a, b = b, a
            
            node = ListNode(gcd(a, b), right)
            left.next = node

            left, right = right, right.next
        
        return head
