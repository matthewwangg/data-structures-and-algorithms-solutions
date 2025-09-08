class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                for n in neighbors:
                    new_i, new_j = i + n[0], j + n[1]
                    if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]) or grid[new_i][new_j] == 0:
                        count += 1
        
        return count
