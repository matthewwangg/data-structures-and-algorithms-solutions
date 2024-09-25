class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle

            if nums[left] <= target and (nums[middle] > target or nums[middle] < nums[left]):
                right = middle - 1
            elif nums[left] >= target and (nums[middle] > target) and nums[middle] < nums[left]:
                right = middle - 1
            else:
                left = middle + 1

        return -1

