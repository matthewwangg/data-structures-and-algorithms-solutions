class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def dfs(current, left, right):
            if left + right == n * 2:
                answer.append(current)

            if left > right:
                dfs(current + ")", left, right + 1)

            if left < n:
                dfs(current + "(", left + 1, right)

        dfs("", 0, 0)
        return answer