class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        currCheckInterval = newInterval

        def overlap(interval, refInterval):
            return ((refInterval[0] <= interval[1]) and (refInterval[1] >= interval[1])) or ((refInterval[1] >= interval[0]) and (refInterval[0] <= interval[0])) or ((refInterval[0] >= interval[0]) and (refInterval[1] <= interval[1]))

        startIdx, endIdx = -1, -1

        for i in range(len(intervals)):
            if overlap(intervals[i], currCheckInterval):
                currCheckInterval = [min(intervals[i][0], currCheckInterval[0]), max(intervals[i][1], currCheckInterval[1])]
                startIdx = i if startIdx == -1 else startIdx
            elif currCheckInterval[1] < intervals[i][0]:
                endIdx = i
                break 
        
        if startIdx != -1 and endIdx != -1:
            return intervals[:startIdx] + [currCheckInterval] + intervals[endIdx:] 
        elif startIdx != -1 and endIdx == -1:
            return intervals[:startIdx] + [currCheckInterval] 
        elif startIdx == -1 and endIdx != -1:
            return intervals[:endIdx] + [currCheckInterval] + intervals[endIdx:]
        else:
            return intervals + [currCheckInterval]
