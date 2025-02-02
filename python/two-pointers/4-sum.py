class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        answers = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                left, right = j + 1, len(nums) - 1
                while left < right:
                    summation = nums[i] + nums[j] + nums[left] + nums[right]
                    if summation == target:
                        answers.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    if summation > target:
                        right -= 1
                    if summation < target:
                        left += 1

        return list(answers)



