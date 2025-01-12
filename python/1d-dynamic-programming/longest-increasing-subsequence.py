class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        array = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    array[i] = max(array[j] + 1, array[i])

        return max(array)
