class Solution:
    def jump(self, nums: List[int]) -> int:
        current, farthest = 0, 0
        finalanswer = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, nums[i] + i)
            if i == current:
                current = farthest
                finalanswer += 1

        return finalanswer