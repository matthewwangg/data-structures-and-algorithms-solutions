class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        current = intervals[0]
        finalanswer = []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= current[1]:
                current[1] = max(current[1], intervals[i][1])
            else:
                finalanswer.append(current)
                current = intervals[i]

        if current not in finalanswer:
            finalanswer.append(current)

        return finalanswer

