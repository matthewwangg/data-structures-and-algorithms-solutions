class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
            
        visited = set(deadends)

        q = deque()
        q.append(("0000", 0))
        visited.add("0000")
        
        while q:
            current, turns = q.popleft()

            if current == target:
                return turns
            
            for i in range(4):
                if current[i] != "9":
                    increment = str(int(current[i])+1)
                else:
                    increment = "0"
                
                if current[i] != "0":
                    decrement = str(int(current[i])-1)
                else:
                    decrement = "9"

                next_up, next_down = current[:i] + increment + current[i+1:], current[:i] + decrement + current[i+1:]

                if next_up not in visited:
                    visited.add(next_up)
                    q.append((next_up, turns+1))
                
                if next_down not in visited:
                    visited.add(next_down)
                    q.append((next_down, turns+1))

        return -1
