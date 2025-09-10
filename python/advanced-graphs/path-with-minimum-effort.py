import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        adj = defaultdict(dict)
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                for n in neighbors:
                    neighbor_i = n[0] + i
                    neighbor_j = n[1] + j

                    if neighbor_i < 0 or neighbor_j < 0 or neighbor_i >= len(heights) or neighbor_j >= len(heights[0]):
                        continue
                    
                    adj[(i, j)][(neighbor_i, neighbor_j)] = abs(heights[i][j] - heights[neighbor_i][neighbor_j])
                    adj[(neighbor_i, neighbor_j)][(i, j)] = abs(heights[i][j] - heights[neighbor_i][neighbor_j])
        
        visited = set()
        heap = []
        heapq.heappush(heap, (0, 0, 0))

        while heap:
            effort, i, j = heapq.heappop(heap)

            if (i, j) in visited:
                continue
            
            visited.add((i, j))

            if (i, j) == (len(heights)-1, len(heights[0])-1):
                return effort
            
            for n in neighbors:
                new_i = n[0] + i
                new_j = n[1] + j
                if new_i < 0 or new_j < 0 or new_i >= len(heights) or new_j >= len(heights[0]) or (new_i, new_j) in visited:
                    continue

                heapq.heappush(heap, (max(effort, abs(heights[i][j] - heights[new_i][new_j])), new_i, new_j))
