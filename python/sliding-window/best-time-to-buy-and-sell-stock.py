class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        lowest = float('inf')
        for i in prices:
            lowest = min(lowest, i)
            answer = max(i - lowest, answer)

        return answer