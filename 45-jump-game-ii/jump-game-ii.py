class Solution:
    def min_jumps(self, a, curr_pos, dp):
        if curr_pos == len(a)-1:
            return 0

        if dp[curr_pos] is not None:
            return dp[curr_pos]

        min_jumps = float('inf')
        max_leap = min(a[curr_pos], len(a)-curr_pos-1)
        for leap in range(1, max_leap+1):
            min_jumps = min(min_jumps, 1+self.min_jumps(a, curr_pos+leap, dp))
        
        dp[curr_pos] = min_jumps
        return min_jumps 

    def jump(self, a: List[int]) -> int:
        n = len(a)
        dp = [None]*n
        dp[n-1] = 0

        for curr_pos in range(n-2, -1, -1):
            min_jumps = float('inf')
            max_leap = min(a[curr_pos], len(a)-curr_pos-1)
            for leap in range(1, max_leap+1):
                min_jumps = min(min_jumps, 1+dp[curr_pos+leap])
            dp[curr_pos] = min_jumps            

        return dp[0]