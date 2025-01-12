class Solution:
    def climbStairs(self, n: int) -> int:
        prev1, prev2 = 0, 1
        for i in range(n):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current

        return prev2
