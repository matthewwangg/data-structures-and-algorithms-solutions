class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()
        newintervals = []
        added = False
        for i in intervals:
            if i[1] < newInterval[0] or added:
                newintervals.append(i)
            else:
                newInterval[0] = min(i[0], newInterval[0])

                if i[0] > newInterval[1]:
                    newintervals.append(newInterval)
                    newintervals.append(i)
                    added = True
                else:
                    newInterval[1] = max(i[1], newInterval[1])

        if not added:
            newintervals.append(newInterval)

        return newintervals