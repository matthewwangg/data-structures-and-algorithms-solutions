class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        distance = len(nums) + 1
        left = 0
        subarraySum = 0
        for i, num in enumerate(nums):
            subarraySum += num
            while subarraySum >= target:
                distance = min(distance, i - left + 1)
                subarraySum -= nums[left]
                left += 1

        if distance == len(nums) + 1:
            return 0

        return distance


