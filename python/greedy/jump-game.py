class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current = nums[0]
        for i in range(len(nums)):
            if i > current:
                return False
            current = max(current, nums[i]+i)

        return True