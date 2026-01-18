from collections import deque

class Solution:
    def isBalanced(self, s, idx, cnt, dp):
        n =len(s)
        if cnt < 0:
            dp[idx][cnt+n] = False
            return dp[idx][cnt+n]
        
        if idx == len(s):
            dp[idx][cnt+n] = (cnt==0)
            return dp[idx][cnt+n]
        
        if dp[idx][cnt+n] is not None:
            return dp[idx][cnt+n] 

        if s[idx]=="(":
            dp[idx][cnt+n] = self.isBalanced(s, idx+1, cnt+1, dp)
        elif s[idx]==")":
            dp[idx][cnt+n] = self.isBalanced(s, idx+1, cnt-1, dp)
        else:
            dp[idx][cnt+n] = (self.isBalanced(s, idx+1, cnt+1, dp) or self.isBalanced(s, idx+1, cnt-1, dp) or self.isBalanced(s, idx+1, cnt, dp))
        
        return dp[idx][cnt+n] 

    def checkValidString(self, s: str) -> bool:
        idx, cnt = 0, 0
        dp = [[None]*(2*len(s)+1)  for _ in range(len(s)+1)]
        return self.isBalanced(s, idx, cnt, dp)