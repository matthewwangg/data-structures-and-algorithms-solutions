class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nearest = {}
        answer = []
        for i in range(30, 101):
            nearest[i] = -1

        reverse = temperatures[::-1]
        for i in range(len(reverse)):
            neighbor = float('-inf')
            for j in range(reverse[i] + 1, 101):
                if nearest[j] != -1:
                    neighbor = max(neighbor, nearest[j])

            if neighbor > float('-inf'):
                answer.append(i - neighbor)
            else:
                answer.append(0)

            nearest[reverse[i]] = i

        return answer[::-1]