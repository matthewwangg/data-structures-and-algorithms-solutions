class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(current):
            if current > amount:
                return float('inf')
            if current == amount:
                return 0
            if current in cache:
                return cache[current]

            cache[current] = float('inf')
            for coin in coins:
                cache[current] = min(cache[current], dfs(current + coin) + 1)

            return cache[current]

        answer = dfs(0)
        if answer < float('inf'):
            return answer

        return -1
