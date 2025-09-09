class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        left = []
        current_sum = 0
        for i in range(len(piles)-1, -1, -1):
            current_sum += piles[i]
            left.append(current_sum)
        left = left[::-1]
        
        cache = {}
        def compute(i, m):
            if i >= len(piles):
                return 0

            if i + 2 * m >= len(piles):
                return left[i]
            
            if (i, m) in cache:
                return cache[(i, m)]
            
            cache[(i, m)] = 0
            for index in range(i, i + 2*m):
                cache[(i, m)] = max(cache[(i, m)], left[i] - compute(index+1, max(m, index-i+1)))

            return cache[(i, m)]

        return compute(0, 1)
