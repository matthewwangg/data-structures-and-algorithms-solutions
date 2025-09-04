class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = set()

        def construct(i, current):
            if len(current) == k:
                combinations.add(tuple(current))
                return

            for num in range(i + 1, n + 1):
                construct(num, current + [num])

        construct(0, [])

        return list(combinations)
