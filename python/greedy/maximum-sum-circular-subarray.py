class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maximum, minimum = float('-inf'), float('inf')
        current_max, current_min = float('-inf'), float('inf')
        total = 0

        for num in nums:
            total += num

            current_max, current_min = max(current_max + num, num), min(current_min + num, num)
            maximum, minimum = max(current_max, maximum), min(current_min, minimum)

        if total - minimum == 0:
            return maximum
            
        return max(maximum, total - minimum)
