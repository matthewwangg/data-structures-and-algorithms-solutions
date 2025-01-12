class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = 1
        minimum = 1

        answer = float('-inf')
        for i in range(len(nums)):
            if nums[i] != 0:
                maximum, minimum = max(maximum * nums[i], minimum * nums[i], nums[i]), min(maximum * nums[i],
                                                                                           minimum * nums[i], nums[i])
                answer = max(maximum, answer)
            else:
                answer = max(answer, 0)
                maximum = 1
                minimum = 1

        return answer

