class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False

        side_length = sum(matchsticks) // 4
        cache = {}

        def construct(i, side1, side2, side3, side4):
            if side1 == side_length and side2 == side_length and side3 == side_length and side4 == side_length and i == len(
                    matchsticks):
                return True

            if side1 > side_length or side2 > side_length or side3 > side_length or side4 > side_length or i == len(
                    matchsticks):
                return False

            key = (i, tuple(sorted([side1, side2, side3, side4])))

            if key in cache:
                return cache[key]

            cache[key] = construct(i + 1, side1 + matchsticks[i], side2, side3, side4) or construct(i + 1, side1,
                                                                                                    side2 + matchsticks[
                                                                                                        i], side3,
                                                                                                    side4) or construct(
                i + 1, side1, side2, side3 + matchsticks[i], side4) or construct(i + 1, side1, side2, side3,
                                                                                 side4 + matchsticks[i])
            return cache[key]

        return construct(0, 0, 0, 0, 0)
