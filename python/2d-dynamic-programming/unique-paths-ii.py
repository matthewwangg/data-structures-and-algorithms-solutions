class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
            
        paths = [[0 for _ in range(len(obstacleGrid[0])+1)] for _ in range(len(obstacleGrid)+1)]

        paths[1][1] = 1
        
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    continue

                paths[i+1][j+1] += paths[i+1][j] + paths[i][j+1]
        
        return paths[-1][-1]
