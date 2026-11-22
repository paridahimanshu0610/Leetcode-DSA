class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.sort()
        currInterval = newInterval.copy()
        res = []
        
        for i in range(len(intervals)):
            tempInterval = intervals[i]

            if len(currInterval) > 0:
                if (tempInterval[0] <= currInterval[0] <= tempInterval[1]) or (tempInterval[0] <= currInterval[1] <= tempInterval[1]) or ((currInterval[0] < tempInterval[0]) and (currInterval[1] > tempInterval[1])):
                    currInterval = [min(tempInterval[0], currInterval[0]), max(tempInterval[1], currInterval[1])]
                elif currInterval[1] < tempInterval[0]:
                    res.append(currInterval)
                    res.append(tempInterval)
                    currInterval = []
                else:
                    res.append(tempInterval)
            else:
                res.append(tempInterval)

        if currInterval:
            res.append(currInterval)

        return res