class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        nums.sort()
        last_index = {}
        for i, num in enumerate(nums):
            last_index[num] = i

        subset_sum = 0
        subsets_list = []

        def subsets(i, current):
            if current:
                subsets_list.append(tuple(current))

            if i == len(nums):
                return

            for index, num in enumerate(nums[i:]):
                subsets(i + index + 1, current + [num])

        subsets(0, [])

        for subset in subsets_list:
            value = 0
            for element in subset:
                value ^= element
            subset_sum += value

        return subset_sum
