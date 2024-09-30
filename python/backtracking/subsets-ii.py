class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sets = set()

        def backtracker(remaining, construct):
            if not remaining:
                sets.add(tuple(sorted(construct[:])))
                return

            backtracker(remaining[1:][:], construct)
            backtracker(remaining[1:][:], construct + [remaining[0]])

        finalanswer = []
        backtracker(nums, [])
        for i in sets:
            finalanswer.append(list(i))

        return finalanswer