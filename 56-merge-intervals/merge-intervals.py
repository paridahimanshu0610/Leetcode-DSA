class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        currInterval = intervals[0]
        res = []
        
        def overlap(interval, refInterval):
            return ((refInterval[0] <= interval[1]) and (refInterval[1] >= interval[1])) or ((refInterval[1] >= interval[0]) and (refInterval[0] <= interval[0])) or ((refInterval[0] >= interval[0]) and (refInterval[1] <= interval[1]))

        for i in range(1, len(intervals)):
            if overlap(currInterval, intervals[i]):
                currInterval = [min(currInterval[0], intervals[i][0]), max(currInterval[1], intervals[i][1])]
            else:
                res.append(currInterval)
                currInterval = intervals[i]
        
        res.append(currInterval)

        return res 