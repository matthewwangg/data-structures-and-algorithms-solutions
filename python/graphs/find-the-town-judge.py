class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = {}
        outdegree = {}
        for t in trust:
            indegree[t[1]] = indegree.get(t[1], 0) + 1
            outdegree[t[0]] = outdegree.get(t[0], 0) + 1
        
        for i in range(1, n+1):
            if indegree.get(i, 0) == n-1 and outdegree.get(i, 0) == 0:
                return i
        
        return -1
