class Solution:
    def largestDivisibleSubset(self, a: List[int]) -> List[int]:
        a.sort()
        n = len(a)
        
        dp = [1] * n
        track = [None] * n
        maxLen = 1
        curr_idx = 0

        for idx in range(n):
            for prev_idx in range(idx):
                if (a[idx] % a[prev_idx] == 0) and (1 + dp[prev_idx] > dp[idx]):
                    dp[idx] = 1 + dp[prev_idx]
                    track[idx] = prev_idx
            if dp[idx] > maxLen:
                maxLen = dp[idx]
                curr_idx = idx

        res = []
        while curr_idx is not None:
            res.append(a[curr_idx])
            curr_idx = track[curr_idx]

        return res