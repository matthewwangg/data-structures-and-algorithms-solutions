class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        finalanswer = float('-inf')
        current = float('-inf')
        for i in nums:
            current = max(current + i, i)
            finalanswer = max(finalanswer, current)

        return finalanswer

