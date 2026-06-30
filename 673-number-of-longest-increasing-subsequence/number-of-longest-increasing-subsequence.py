class Solution:
    def findNumberOfLIS(self, a: List[int]) -> int:
        n = len(a)
        dp = [1] * n
        cnt_track = [1] * n
        maxLen = 1
        cnt = 1

        for idx in range(n):
            currMaxLen, currCnt = 1, 1
            for prev_idx in range(idx):
                if (a[idx] > a[prev_idx]):
                    if (1 + dp[prev_idx] >= dp[idx]):
                        dp[idx] = 1 + dp[prev_idx]
                        if dp[idx] > currMaxLen:
                            currMaxLen = dp[idx]
                            currCnt = cnt_track[prev_idx]
                        elif dp[idx] == currMaxLen:
                            currCnt += cnt_track[prev_idx]

            cnt_track[idx] = currCnt
            if currMaxLen > maxLen:
                maxLen = currMaxLen

        # print(maxLen, dp, cnt_track)
        cnt = 0
        for i in range(n):
            if dp[i] == maxLen:
                cnt += cnt_track[i]

        return cnt