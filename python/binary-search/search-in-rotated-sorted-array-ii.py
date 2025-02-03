class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            middle = (left + right) // 2
            if nums[middle] == target:
                return True

            if nums[left] <= nums[middle] <= nums[right]:
                if nums[middle] > target:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[left] <= nums[middle]:
                    if nums[middle] > target and nums[right] < target:
                        right = middle - 1
                    else:
                        left = middle + 1
                else:
                    if nums[middle] < target and nums[right] >= target:
                        left = middle + 1
                    else:
                        right = middle - 1

        return False
