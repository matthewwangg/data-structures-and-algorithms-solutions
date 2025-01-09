import heapq


class MedianFinder:

    def __init__(self):
        self.above = []
        self.below = []
        self.count = 0

    def addNum(self, num: int) -> None:
        if self.count:
            below = -heapq.heappop(self.below)
            if self.count % 2 == 0:
                heapq.heappush(self.below, -below)
                above = heapq.heappop(self.above)
                if num > above:
                    heapq.heappush(self.below, -above)
                    heapq.heappush(self.above, num)
                else:
                    heapq.heappush(self.above, above)
                    heapq.heappush(self.below, -num)
            else:
                if num > below:
                    heapq.heappush(self.below, -below)
                    heapq.heappush(self.above, num)
                else:
                    heapq.heappush(self.above, below)
                    heapq.heappush(self.below, -num)
        else:
            heapq.heappush(self.below, -num)

        self.count += 1

    def findMedian(self) -> float:
        if self.count % 2 == 0:
            below = -heapq.heappop(self.below)
            above = heapq.heappop(self.above)
            heapq.heappush(self.above, above)
            median = (below + above) / 2
        else:
            below = -heapq.heappop(self.below)
            median = below

        heapq.heappush(self.below, -below)

        return median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()