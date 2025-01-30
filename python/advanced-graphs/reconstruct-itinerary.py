class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(lambda: [])
        for u, v in tickets:
            adj[u].append(v)

        for location in adj:
            adj[location].sort()
            adj[location] = adj[location][::-1]

        order = []

        def dfs(curr):
            while len(adj[curr]) > 0:
                dfs(adj[curr].pop())
            order.append(curr)

        dfs("JFK")
        return order[::-1]

