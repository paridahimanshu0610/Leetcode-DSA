class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False]*n
        dp[0] = True
        currJumps = 0 # Total possible jumps from the previous index to reach the current index

        for i in range(1, n):
            if i >= minJump:
                currJumps += dp[i-minJump]
            if i > maxJump:
                currJumps -= dp[i-maxJump-1]

            dp[i] = (s[i]=="0") and (currJumps>0)

        return dp[-1]