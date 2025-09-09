class Solution:
    def candy(self, ratings: List[int]) -> int:
        constraints = [1 for _ in range(len(ratings))]

        for i in range(len(ratings)):
            if i > 0 and ratings[i-1] < ratings[i]:
                constraints[i] = float('-inf')

            if i < len(ratings)-1 and ratings[i+1] < ratings[i]:
                constraints[i] = float('-inf')

        for i in range(len(constraints)):
            if constraints[i] != 1:
                if i > 0 and ratings[i-1] < ratings[i]:
                    constraints[i] = max(constraints[i], constraints[i-1]+1)

        for i in range(len(constraints)-1, -1, -1):
            if constraints[i] != 1:
                if i < len(ratings)-1 and ratings[i+1] < ratings[i]:
                    constraints[i] = max(constraints[i], constraints[i+1]+1)

        return sum(constraints)
