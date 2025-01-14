class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        duration = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        while q:
            current = q.popleft()
            if current[0] < 0 or current[1] < 0 or current[0] >= len(grid) or current[1] >= len(grid[0]) or (
                    grid[current[0]][current[1]] != 2 and grid[current[0]][current[1]] != 1):
                continue

            grid[current[0]][current[1]] = 3
            duration = max(duration, current[2])

            for neighbor in neighbors:
                q.append((current[0] + neighbor[0], current[1] + neighbor[1], current[2] + 1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return duration