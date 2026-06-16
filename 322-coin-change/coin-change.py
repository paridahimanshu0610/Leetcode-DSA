class Solution:
    def compare(self, n1, n2):
        if n1 >= 0 and n2 >= 0:
            return min(n1, n2)
        elif n1 >= 0:
            return n1
        elif n2 >= 0:
            return n2
        else:
            return -1

    def soFar(self, a, idx, k, dp):
        if idx < 0:
            return -1
        elif k == 0:
            dp[idx][k] = 0
            return 0

        if dp[idx][k] is not None:
            return dp[idx][k]
        
        notTake = self.soFar(a, idx-1, k, dp)
        take = -1
        if a[idx] <= k:
            temp1, temp2 = self.soFar(a, idx, k - a[idx], dp), self.soFar(a, idx-1, k - a[idx], dp)
            temp = self.compare(temp1, temp2)
            take = (1 + temp) if temp >= 0 else -1
        
        dp[idx][k] = self.compare(take, notTake)
 
        return dp[idx][k]

    def coinChange(self, a: List[int], amount: int) -> int:
        n = len(a)
        dp = [-1]*(amount+1)
        
        for idx in range(1, n+1):
            temp = [-1]*(amount+1)
            temp[0] = 0
            for k in range(1, amount+1):
                notTake = dp[k]
                take = -1
                if a[idx-1] <= k:
                    temp1, temp2 = temp[k-a[idx-1]], dp[k-a[idx-1]]
                    minVal = self.compare(temp1, temp2)
                    take = (1+minVal) if minVal >= 0 else -1
                temp[k] = self.compare(take, notTake)
            dp = temp

        return dp[amount]
