class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        power_of_2 = max(2**((n // 2) - 1) * (2 + n % 2), 2**(n // 2) * (n % 2))
        power_of_3 = max(3**((n // 3) - 1) * (3 + n % 3), 3**(n // 3) * (n % 3))

        return max(power_of_2, power_of_3)
