class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(dict)

        for i, equation in enumerate(equations):
            adj[equation[0]][equation[1]] = values[i]
            adj[equation[1]][equation[0]] = 1/values[i]

        answers = []
        for dividend, divisor in queries:
            result = -1
            visited = set()
            q = deque()

            if dividend in adj:
                q.append((dividend, 1.0))
                
            while q:
                current, value = q.popleft()

                if current == divisor:
                    if value != result and result != -1:
                        result = -1
                        break
                    
                    result = value
                    continue

                if current in visited:
                    continue
                
                visited.add(current)

                for neighbor in adj.get(current, []):
                    q.append((neighbor, adj[current][neighbor] * value))
            
            answers.append(result)

        return answers
