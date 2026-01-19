class Solution:
    def isReachable(self, a, idx, dp):
        if idx == len(a)-1:
            return True

        max_leap = min(a[idx], len(a)-idx-1)
        for leap in range(1, max_leap+1):
            dp[idx][leap-1] = self.isReachable(a, idx+leap, dp) if dp[idx][leap-1] is None else dp[idx][leap-1]
            if dp[idx][leap-1]:
                return True

        return False


    def canJump(self, a: List[int]) -> bool:
        if len(a)==1:
            return True
        
        max_leap = a[0]
        for i in range(1, len(a)):
            if max_leap==0:
                return False
            max_leap = max(a[i], max_leap-1)

        return True