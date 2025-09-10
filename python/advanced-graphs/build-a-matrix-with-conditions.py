class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        matrix = [[0 for _ in range(k)] for _ in range(k)]

        deps_row = defaultdict(list)
        indegree_row = defaultdict(int)

        deps_col = defaultdict(list)
        indegree_col = defaultdict(int)
        
        for above, below in rowConditions:
            deps_row[below].append(above)
            indegree_row[above] += 1
        
        for left, right in colConditions:
            deps_col[right].append(left)
            indegree_col[left] += 1

        def topoSort(deps, indegree):
            index = {}
            current_index = k-1

            q = deque()

            for i in range(1, k+1):
                if not indegree[i]:
                    q.append(i)

            while q:
                current = q.popleft()
                index[current] = current_index
                current_index -= 1

                for dependent in deps[current]:
                    indegree[dependent] -= 1
                    if indegree[dependent] == 0:
                        q.append(dependent)
            
            return index
        
        index_row = topoSort(deps_row, indegree_row)
        index_col = topoSort(deps_col, indegree_col)

        if len(index_row) != k or len(index_col) != k:
            return []
        
        for key in index_row:
            matrix[index_row[key]][index_col[key]] = key
        
        return matrix
