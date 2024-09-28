# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for currentnode in lists:
            while currentnode:
                heapq.heappush(heap, currentnode.val)
                currentnode = currentnode.next

        head = ListNode(0)
        current = head
        while len(heap) > 0:
            current.next = ListNode(heapq.heappop(heap))
            current = current.next

        return head.next
