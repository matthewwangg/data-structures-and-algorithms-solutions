import queue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = queue.PriorityQueue()

        for i in nums:
            q.put(-i)

        for i in range(k):
            current = -q.get()

        return current