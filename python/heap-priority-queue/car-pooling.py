import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        for trip in trips:
            heapq.heappush(heap, (trip[1], trip[0]))
            heapq.heappush(heap, (trip[2], -trip[0]))

        space_used = 0
        while heap:
            time, diff = heapq.heappop(heap)

            space_used += diff
            if space_used > capacity:
                return False

        return True
