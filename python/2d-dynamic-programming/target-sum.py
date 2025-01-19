class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def count(current, i):
            if i == len(nums):
                if current == target:
                    return 1
                else:
                    return 0

            if (current, i) in cache:
                return cache[(current, i)]

            cache[(current, i)] = count(current + nums[i], i + 1) + count(current - nums[i], i + 1)

            return cache[(current, i)]

        return count(0, 0)



