class Solution:
    def get_min_jumps(self, a, idx, dp):
        n = len(a)
        if idx == n-1:
            return 0

        if dp[idx] is not None:
            return dp[idx]

        max_leap = min(n-idx-1, a[idx])
        min_jumps = float('inf')
        for leap in range(max_leap, 0, -1):
            next_idx = idx+leap
            min_jumps = min(min_jumps, 1 + self.get_min_jumps(a, next_idx, dp)) 

        dp[idx] = min_jumps
        return dp[idx]

    def jump(self, a: List[int]) -> int:
        n = len(a)
        l, r = (0, 0)
        jumps = 0

        while r < n-1:
            max_reach = -1
            for idx in range(l, r+1):
                max_reach = min(max(max_reach, idx+a[idx]), n-1)

            l, r = (r+1, max_reach)
            jumps += 1

        return jumps