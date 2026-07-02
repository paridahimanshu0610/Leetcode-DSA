class Solution:
    def cutCost(self, a, l, h, n, dp):
        if l > h:
            return 0

        if dp[l][h] is not None:
            return dp[l][h]

        leftLastCut = a[l-1] if l-1 >= 0 else 0
        rightLastCut = a[h+1] if h+1 < len(a) else n
        currLen = rightLastCut - leftLastCut

        mini = float('inf')
        for i in range(l, h+1):
            currCost = currLen + self.cutCost(a, l, i-1, n, dp) + self.cutCost(a, i+1, h, n, dp)
            mini = min(mini, currCost)

        dp[l][h] = mini

        return dp[l][h]

    def minCost(self, n: int, a: List[int]) -> int:
        a.sort()
        m = len(a)
        dp = [[0] * m for _ in range(m)]

        for currItems in range(1, m+1):
            for l in range(0, m-currItems+1):
                h = l+currItems-1
                mini = float('inf')

                leftLastCut = a[l-1] if l-1 >= 0 else 0
                rightLastCut = a[h+1] if h+1 < len(a) else n
                currLen = rightLastCut - leftLastCut 

                for i in range(l, h+1):
                    leftPart = dp[l][i-1] if i-1 >= 0 else 0
                    rightPart = dp[i+1][h] if i+1 < m else 0

                    currCost = currLen + leftPart + rightPart
                    mini = min(mini, currCost)
                
                dp[l][h]  = mini

        return dp[0][m-1]