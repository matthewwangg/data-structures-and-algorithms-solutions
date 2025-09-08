class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1

        numbers = [0 for _ in range(n+1)]
        numbers[1], numbers[2] = 1, 1

        for i in range(3, n+1):
            numbers[i] = numbers[i-1] + numbers[i-2] + numbers[i-3]
        
        return numbers[n]
