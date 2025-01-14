class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        maximum = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < maximum:
                count += 1
                maximum = min(maximum, intervals[i][1])
            else:
                maximum = max(maximum, intervals[i][1])

        return count

