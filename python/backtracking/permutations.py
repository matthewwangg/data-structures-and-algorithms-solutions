class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = set()

        def backtracker(remaining, constructed):
            if len(remaining) == 0:
                answer.add(tuple(constructed[:]))
                return

            current = set(list(remaining)[:])

            for i in remaining:
                current.remove(i)
                backtracker(current, constructed + [i])
                current.add(i)

        remaining = set(nums)
        backtracker(remaining, [])
        finalanswer = []
        for i in answer:
            finalanswer.append(list(i))
        return finalanswer