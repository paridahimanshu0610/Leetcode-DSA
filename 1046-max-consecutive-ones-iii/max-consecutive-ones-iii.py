class Solution:
    def longestOnes(self, a: List[int], k: int) -> int:
        l, r = 0, 0
        curr_left = k
        curr_streak, res = 0, 0

        while l <= r and r < len(a):
            if a[r] == 1:
                curr_streak += 1
            else:
                while l < r and curr_left <= 0:
                    if a[l]==0:
                        curr_left = min(curr_left+1, k)
                    curr_streak = max(curr_streak-1, 0)
                    l += 1

                if curr_left > 0:
                    curr_streak += 1
                    curr_left -= 1
            r += 1
            res = max(res, curr_streak)
        
        return res