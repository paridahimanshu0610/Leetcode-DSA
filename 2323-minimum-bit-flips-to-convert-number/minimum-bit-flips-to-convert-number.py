class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        temp = start ^ goal
        res = 0

        while temp > 1:
            if temp%2==1:
                res += 1
            temp = int(temp/2)
        
        if temp==1:
            res += 1

        return res