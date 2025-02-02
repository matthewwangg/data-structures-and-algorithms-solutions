class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[first]:
                nums[first + 1] = nums[i]
                first += 1

        return first + 1

