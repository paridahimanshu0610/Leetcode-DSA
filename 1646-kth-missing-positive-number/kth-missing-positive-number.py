class Solution:
    def findKthPositive(self, a: List[int], k: int) -> int:
        missingCnt = 0
        i, itr = 0, 1

        while missingCnt < k and i < len(a):
            if itr == a[i]:
                i += 1
            else:
                missingCnt += 1

            itr += 1

        if missingCnt < k:
            return a[-1] + (k-missingCnt) 
        else:
            return itr-1