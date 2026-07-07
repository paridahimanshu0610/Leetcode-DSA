class Solution:
    def fromHere(self, a, idx, cap, canBuy, dp):
        if idx == len(a):
            return 0
        if cap == -1:
            return 0

        if dp[idx][cap][canBuy] is not None:
            return dp[idx][cap][canBuy]

        if canBuy==1:
            res = max(-a[idx]+self.fromHere(a, idx+1, cap, 0, dp), self.fromHere(a, idx+1, cap, 1, dp))
        else:
            res = max(a[idx]+self.fromHere(a, idx+1, cap-1, 1, dp), self.fromHere(a, idx+1, cap, 0, dp))
        
        dp[idx][cap][canBuy] = res

        return res

    def maxProfit(self, a: List[int]) -> int:
        n = len(a)
        dp = [[0]*2 for _ in range(2)]

        for idx in range(n-1, -1, -1):
            temp = [[0]*2 for _ in range(2)] 
            for cap in range(2):
                for canBuy in {0, 1}:
                    if canBuy==1:
                        res = max(-a[idx]+dp[cap][0], dp[cap][1])
                    else:
                        temp1 = dp[cap-1][1] if (cap-1>=0) else 0 
                        res = max(a[idx]+temp1, dp[cap][0])
                    temp[cap][canBuy] = res

            dp = temp                    
        
        return dp[1][1]