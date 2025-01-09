import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.size = k
        for i in nums:
            heapq.heappush(self.heap, i)

        for i in range(len(nums) - k):
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.size:
            heapq.heappop(self.heap)
        kth = heapq.heappop(self.heap)
        heapq.heappush(self.heap, kth)
        return kth

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)