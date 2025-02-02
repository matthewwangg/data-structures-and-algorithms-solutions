class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            correct = nums[i] - 1
            while nums[i] > 0 and nums[i] < len(nums) and nums[correct] != nums[i]:
                nums[i], nums[correct] = nums[correct], nums[i]
                correct = nums[i] - 1

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1

        return len(nums) + 1





