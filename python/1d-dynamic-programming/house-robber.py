class Solution:
    def rob(self, nums: List[int]) -> int:
        firstcost, secondcost = 0, 0
        for i in nums:
            currentdecision = max(firstcost + i, secondcost)
            firstcost = secondcost
            secondcost = currentdecision

        return currentdecision
