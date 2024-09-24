class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = {"(": ")", "{": "}", "[": "]"}
        for i in s:
            if i in left.keys():
                stack.append(i)
            else:
                if len(stack) > 0 and left[stack[-1]] == i:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
