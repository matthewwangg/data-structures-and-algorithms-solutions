import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(lambda: [])
        for u, v, w in times:
            adj[u].append((w, v))

        heap = []
        distance = {}
        for i in range(1, n + 1):
            distance[i] = float('inf')

        distance[k] = 0
        heapq.heappush(heap, (0, k))
        visited = set()

        while heap:
            dist, node = heapq.heappop(heap)

            if node in visited:
                continue

            distance[node] = dist
            visited.add(node)

            for weight, neighbor in adj[node]:
                heapq.heappush(heap, (dist + weight, neighbor))

        time = float('-inf')
        for node in distance:
            time = max(distance[node], time)

        if time == float('inf'):
            return -1

        return time



