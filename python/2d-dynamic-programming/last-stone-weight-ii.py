class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        cache = {}
        def compute(i, value):
            if i == len(stones) and value >= 0:
                return value
            
            if i == len(stones):
                return float('inf')
            
            if (i, value) in cache:
                return cache[(i, value)]
            
            cache[(i, value)] = min(compute(i+1, value - stones[i]), compute(i+1, value + stones[i]))

            return cache[(i, value)]
        
        return compute(0, 0)
