class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(set)
        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
        
        roots = set()
        for i in range(n):
            roots.add(i)

        leaves = [node for node in range(n) if len(adj[node]) == 1]

        while len(roots) > 2:
            new_leaves = []

            for leaf in leaves:
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                roots.remove(leaf)

                if len(adj[neighbor]) == 1:
                    new_leaves.append(neighbor)
            
            leaves = new_leaves

        return list(roots)
