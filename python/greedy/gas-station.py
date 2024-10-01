class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        worststart = 0
        minimumnet = gas[0] - cost[0]
        totalnet = 0
        for i in range(len(gas)):
            totalnet += gas[i]
            totalnet -= cost[i]
            if totalnet <= minimumnet:
                worststart = i
                minimumnet = totalnet

        if totalnet < 0:
            return -1

        if worststart == len(gas) - 1:
            return 0
        else:
            return worststart + 1