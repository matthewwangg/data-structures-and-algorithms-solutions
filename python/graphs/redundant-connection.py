class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        MST = []
        connected = {}
        for e in edges:
            connected[e[0]] = False
            connected[e[1]] = False

        leaveout = []
        for i in range(len(edges) - 1, -1, -1):
            inputs = edges[:i] + edges[i + 1:]
            print(inputs)
            if self.validTree(len(edges) + 1, inputs):
                return edges[i]

        return []

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbors = {}
        for node in range(n):
            neighbors[node] = set()

        for e in edges:
            neighbors[e[0]].add(e[1])
            neighbors[e[1]].add(e[0])

        connected = {}
        visited = set()
        q = deque()
        q.append(1)
        while q:
            current = q.popleft()
            if current in visited:
                return False
            visited.add(current)
            for neighbor in neighbors[current]:
                if current in neighbors[neighbor]:
                    neighbors[neighbor].remove(current)
                q.append(neighbor)

        return len(visited) == n - 1

