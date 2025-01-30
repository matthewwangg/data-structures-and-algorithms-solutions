class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(lambda: [])
        for u, v, w in flights:
            adj[u].append((w, v))

        distance = [[float('inf') for _ in range(n)] for _ in range(k + 2)]
        distance[0][src] = 0

        for i in range(1, k + 2):
            for j in range(n):
                distance[i][j] = distance[i - 1][j]

            for u, v, w in flights:
                distance[i][v] = min(distance[i][v], distance[i - 1][u] + w)

        if distance[k + 1][dst] == float('inf'):
            return -1

        return distance[k + 1][dst]

