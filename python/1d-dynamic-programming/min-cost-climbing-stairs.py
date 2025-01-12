class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        array = [0] * (len(cost)+2)
        for i in range(len(cost)-1, -1, -1):
            array[i] = cost[i] + min(array[i+1], array[i+2])
        return min(array[0], array[1])