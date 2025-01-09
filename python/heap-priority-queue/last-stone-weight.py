import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)

        while len(heap) >= 2:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x == y:
                continue
            else:
                heapq.heappush(heap, -(y - x))

        if heap:
            return -heapq.heappop(heap)
        else:
            return 0