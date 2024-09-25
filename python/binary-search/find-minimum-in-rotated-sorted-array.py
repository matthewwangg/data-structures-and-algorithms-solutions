class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        answer = float('inf')
        while left <= right:
            middle = (left + right) // 2
            answer = min(answer, nums[middle])
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle - 1
        return answer
