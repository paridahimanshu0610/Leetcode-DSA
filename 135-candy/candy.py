class Solution:
    def candy(self, a: List[int]) -> int:
        i, n = 1, len(a)
        res = 1

        while i < n:
            if a[i] == a[i-1]:
                res += 1
                i += 1
                continue
            
            peak = 1
            while (i < n and a[i] > a[i-1]):
                peak += 1
                res += peak
                i += 1
            
            down = 1
            while (i < n and a[i-1] > a[i]):
                res += down
                i += 1
                down += 1
            
            if down > peak:
                res += (down-peak)

        return res