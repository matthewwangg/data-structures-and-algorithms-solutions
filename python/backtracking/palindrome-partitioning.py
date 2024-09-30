class Solution:
    def partition(self, s: str) -> List[List[str]]:
        finalanswer = []

        def backtracker(remaining, current):
            if not remaining:
                finalanswer.append(current[:])
                return

            temp = ""
            for i in range(len(remaining)):
                temp += remaining[i]
                if temp == temp[::-1]:
                    backtracker(remaining[i + 1:], current + [temp])

        backtracker(s, [])
        return finalanswer
