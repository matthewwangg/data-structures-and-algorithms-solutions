class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        path_sum = [[float('inf') for _ in range(len(grid[0])+1)] for _ in range(len(grid)+1)]
        path_sum[0][1], path_sum[1][0] = 0, 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                path_sum[i+1][j+1] = min(path_sum[i+1][j], path_sum[i][j+1]) + grid[i][j]
        
        return path_sum[-1][-1]
