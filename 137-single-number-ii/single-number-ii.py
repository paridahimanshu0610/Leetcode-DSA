class Solution:
    def singleNumber(self, a: List[int]) -> int:
        res = 0
        bits = 32
        for i in range(32):
            cnt = 0
            for e in a:
                cnt += (e>>i) & 1
            if cnt%3==1:
                res += (1<<i)
        
        if cnt%3==1:
            res = (res-1) & ((1<<bits) - 1)
            res = (~res) & ((1<<bits) - 1)
            res = -res

        return res