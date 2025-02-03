class Solution:
    def decodeString(self, s: str) -> str:
        finalanswer = ""
        stack = []
        for char in s:
            if char == "]":
                string = ""
                while stack[-1] != "[":
                    string += stack.pop()[::-1]
                string = string[::-1]
                stack.pop()
                number = ""
                while stack and stack[-1].isnumeric():
                    number += stack.pop()
                number = number[::-1]
                addition = string * int(number)
                if stack:
                    stack.append(addition)
                else:
                    finalanswer += addition
            else:
                stack.append(char)

        return finalanswer + "".join(stack)

