class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        while n != 1:
            if n in seen:
                return False

            sumofdigits = 0
            for char in str(n):
                sumofdigits += int(char) ** 2

            seen[n] = True
            n = sumofdigits

        return True
