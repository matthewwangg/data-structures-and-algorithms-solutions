class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = set()
        finalanswer = []

        def backtracker(current, sums, index):
            if sums > target:
                return
            if sums == target:
                answer.add(tuple(sorted(current)))
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                current.append(candidates[i])
                backtracker(current, sums + candidates[i], i + 1)
                current.pop()

        backtracker([], 0, 0)
        for i in answer:
            finalanswer.append(list(i))
        return finalanswer