class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        answer = right
        while left <= right:
            middle = (left + right) // 2
            d = 1
            weight = 0
            for w in weights:
                if w + weight > middle:
                    d += 1
                    weight = w
                else:
                    weight += w

            if d > days:
                left = middle + 1
            else:
                answer = min(middle, answer)
                right = middle - 1

        return answer