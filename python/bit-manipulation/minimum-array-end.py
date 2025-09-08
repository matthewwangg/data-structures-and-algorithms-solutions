class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = x
        to_go = n - 1
        index = 1

        while to_go:
            if not (x & index):
                result |= (to_go & 1) * index
                to_go >>= 1
            index <<= 1
    
        return result
