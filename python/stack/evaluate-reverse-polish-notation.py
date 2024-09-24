class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.isnumeric():
                stack.append(int(i))
            elif len(i) > 1 and i[0] == "-":
                stack.append(-(int(i[1:])))
            else:
                first = stack.pop()
                second = stack.pop()
                if i == "+":
                    stack.append(int(first + second))
                elif i == "-":
                    stack.append(int(second - first))
                elif i == "*":
                    stack.append(int(first * second))
                else:
                    stack.append(int(second / first))

        return stack[-1]