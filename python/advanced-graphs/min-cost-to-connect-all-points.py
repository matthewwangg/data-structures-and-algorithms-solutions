import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        adj = defaultdict(lambda: [])
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                adj[i].append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), j))
                adj[j].append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i))

        heapq.heappush(heap, (0, 0))
        visited = set()
        cost = 0
        while len(visited) < len(points):
            distance, node = heapq.heappop(heap)

            if node in visited:
                continue

            cost += distance
            visited.add(node)

            for dist, neighbor in adj[node]:
                heapq.heappush(heap, (dist, neighbor))

        return cost

