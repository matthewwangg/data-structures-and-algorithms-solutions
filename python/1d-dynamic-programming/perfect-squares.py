class Solution:
    def numSquares(self, n: int) -> int:
        count = [float('inf') for _ in range(n+1)]
        count[0] = 0

        nums = []
        for i in range(1, n+1):
            square = i * i
            if square > n:
                break
            nums.append(square)

        for num in nums:
            for i in range(num, len(count)):
                count[i] = min(count[i], count[i-num]+1)

        return count[n]
