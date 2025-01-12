class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]), nums[0])

    def rob_helper(self, nums: List[int]) -> int:
        firstcost, secondcost, currentdecision = 0, 0, 0
        for i in nums:
            currentdecision = max(firstcost + i, secondcost)
            firstcost = secondcost
            secondcost = currentdecision

        return currentdecision
