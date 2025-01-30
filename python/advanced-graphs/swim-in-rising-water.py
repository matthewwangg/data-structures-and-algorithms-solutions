import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        heap = [(grid[0][0], 0, 0)]
        totaltime = 0
        while heap:
            time, i, j = heapq.heappop(heap)

            totaltime = max(totaltime, time)
            visited.add((i, j))

            if (i, j) == (len(grid) - 1, len(grid[0]) - 1):
                return totaltime

            for n in neighbors:
                if i + n[0] < 0 or j + n[1] < 0 or i + n[0] >= len(grid) or j + n[1] >= len(grid[0]) or (
                i + n[0], j + n[1]) in visited:
                    continue
                heapq.heappush(heap, (grid[i + n[0]][j + n[1]], i + n[0], j + n[1]))

        return 0
