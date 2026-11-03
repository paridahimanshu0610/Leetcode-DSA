class Solution:
    def eraseOverlapIntervals(self, a: list[list[int]]) -> int:
        a.sort()
        currStart, currEnd = a[0]
        res = 0

        for i in range(1, len(a)):
            tempStart, tempEnd = a[i]

            if tempStart >= currEnd:
                currStart, currEnd = tempStart, tempEnd
            else:
                res += 1
                if tempEnd <= currEnd:
                    currStart, currEnd = tempStart, tempEnd

        return res