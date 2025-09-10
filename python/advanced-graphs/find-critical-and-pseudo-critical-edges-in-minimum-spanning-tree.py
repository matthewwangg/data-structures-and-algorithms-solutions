class UnionFind:
    def __init__(self, size):
        self.representative = [i for i in range(size)]
        self.size = [1 for _ in range(size)]
    
    def find(self, x):
        if self.representative[x] == x:
            return x
        
        self.representative[x] = self.find(self.representative[x])

        return self.representative[x]
    
    def union(self, a, b):
        representative_a = self.find(a)
        representative_b = self.find(b)

        if representative_a == representative_b:
            return
        
        if self.size[representative_a] >= self.size[representative_b]:
            self.representative[representative_b] = representative_a
            self.size[representative_a] += self.size[representative_b]
        else:
            self.representative[representative_a] = representative_b
            self.size[representative_b] += self.size[representative_a]

import heapq
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        critical = set()
        pseudo_critical = set()

        def kruskal(uf, edges):
            heap = []
            for a, b, w in edges:
                heapq.heappush(heap, (w, a, b))
            
            cost = 0
            count = 0
            while heap:
                weight, a, b = heapq.heappop(heap)

                if uf.find(a) == uf.find(b):
                    continue

                uf.union(a, b) 

                cost += weight
                count += 1
        
            return cost, count
        
        uf = UnionFind(n)
        mst_cost, _ = kruskal(uf, edges)

        for i, edge in enumerate(edges):
            uf = UnionFind(n)
            cost, count = kruskal(uf, edges[:i] + edges[i+1:])
            if cost > mst_cost or count != n - 1:
                critical.add(i)
                
            if i not in critical:
                uf = UnionFind(n)
                uf.union(edge[0], edge[1])

                cost, count = kruskal(uf, edges[:i] + edges[i+1:])
                if cost + edge[2] == mst_cost and count + 1 == n - 1:
                    pseudo_critical.add(i)       

        answer = [list(critical), list(pseudo_critical)]

        return answer
