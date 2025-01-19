class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}

        def dfs(left, right):
            if left < 1 or right < 1 or left > len(nums) - 2 or right > len(nums) - 2:
                return 0

            if (left, right) in cache:
                return cache[(left, right)]

            cache[(left, right)] = 0
            for i in range(left, right + 1):
                cache[(left, right)] = max(cache[(left, right)], nums[i] * nums[left - 1] * nums[right + 1] + dfs(left, i - 1) + dfs(i + 1, right))

            return cache[(left, right)]

        return dfs(1, len(nums) - 2)
