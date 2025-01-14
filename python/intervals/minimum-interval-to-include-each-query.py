import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        answer = []
        lengths = {}
        heap = []

        intervals.sort()
        sorted_queries = queries[:]
        sorted_queries.sort()

        count = 0
        for q in sorted_queries:
            for i in range(count, len(intervals)):
                if intervals[i][0] <= q:
                    heapq.heappush(heap, [intervals[i][1] - intervals[i][0] + 1, intervals[i][0], intervals[i][1]])
                else:
                    count = i
                    break

            if len(heap) == 0:
                lengths[q] = -1
                continue

            current = heapq.heappop(heap)
            while heap and current[2] < q:
                current = heapq.heappop(heap)
            heapq.heappush(heap, current)

            if q <= current[2] and q >= current[1]:
                lengths[q] = current[0]
            else:
                lengths[q] = -1

        for q in queries:
            answer.append(lengths[q])

        return answer


