class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = set()

        def construct(current, remaining):
            if len(current) == len(nums):
                permutations.add(tuple(current))
                return

            for i, num in enumerate(remaining):
                construct(current + [num], remaining[:i] + remaining[i + 1:])

        construct([], nums)

        return list(permutations)
