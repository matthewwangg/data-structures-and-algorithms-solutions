class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = num1[::-1], num2[::-1]
        multiplier1 = 1
        answer = 0
        for i in range(len(n1)):
            multiplier2 = 1
            for j in range(len(n2)):
                answer += int(n1[i]) * multiplier1 * int(n2[j]) * multiplier2
                multiplier2 *= 10
            multiplier1 *= 10
        return str(answer)


