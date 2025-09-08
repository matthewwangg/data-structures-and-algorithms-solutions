class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        count = [0 for _ in range(target+1)]
        count[0] = 1

        for i in range(len(count)):
            for num in nums:
                if i+num >= len(count):
                    continue
                count[i+num] += count[i]
        
        return count[target]
