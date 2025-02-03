class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        rounded = 0
        while left <= right:
            middle = (left + right) // 2
            if middle * middle == x:
                return middle
            if middle * middle < x:
                rounded = max(rounded, middle)
                left = middle + 1
            else:
                right = middle - 1

        return rounded
