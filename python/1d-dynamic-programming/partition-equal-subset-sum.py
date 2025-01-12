class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totaltarget = sum(nums)
        if totaltarget % 2 != 0:
            return False

        totaltarget //= 2

        cache = {}

        def dfs(i, target):
            if target == 0:
                return True
            if i >= len(nums) or target < 0:
                return False
            if (i, target) in cache:
                return cache[(i, target)]

            cache[(i, target)] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            return cache[(i, target)]

        return dfs(0, totaltarget)
