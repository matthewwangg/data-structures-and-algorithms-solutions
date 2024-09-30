class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = set()
        finalanswer = []

        def backtracker(current, sums):
            if sums > target:
                return
            if sums == target:
                answer.add(tuple(sorted(current)))
                return

            for i in candidates:
                backtracker(current[:] + [i], sums + i)

        backtracker([], 0)
        for i in answer:
            finalanswer.append(list(i))
        return finalanswer


