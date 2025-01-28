class Solution:
    def reverseBits(self, n: int) -> int:
        return int("0b" + bin(n)[2:][::-1] + "0" * (32-len(bin(n))+2), 2)
