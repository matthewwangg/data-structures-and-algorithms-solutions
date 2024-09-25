class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = 0
        for i in piles:
            maximum = max(maximum, i)

        minimum = 1
        answer = maximum
        while minimum <= maximum:
            middle = (minimum + maximum) // 2
            hours = 0
            for i in piles:
                if i % middle == 0:
                    hours += i // middle
                else:
                    hours += (i // middle) + 1

            if hours > h:
                minimum = middle + 1
            else:
                answer = min(answer, middle)
                maximum = middle - 1

        return answer
