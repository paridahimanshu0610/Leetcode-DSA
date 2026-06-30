class Solution:
    def longestStrChain(self, a: List[str]) -> int:
        a.sort(key = lambda x: len(x))

        def isPredecessor(pred, suc):
            if (len(suc) - len(pred)) != 1:
                return False
            
            pred_idx, suc_idx = 0, 0
            cnt = 0
            while suc_idx < len(suc) and pred_idx < len(pred):
                if pred[pred_idx] == suc[suc_idx]:
                    pred_idx += 1
                else:
                    cnt += 1

                if cnt > 1:
                    return False
                
                suc_idx += 1
            
            return cnt <= 1

        n = len(a)
        dp = [1] * n
        # track = [None] * n
        # curr_idx = 0
        maxLen = 1

        for idx in range(n):
            for prev_idx in range(idx):
                if isPredecessor(a[prev_idx], a[idx]) and (1 + dp[prev_idx]) > dp[idx]:
                    dp[idx] = 1 + dp[prev_idx]
                    # track[idx] = prev_idx

            if dp[idx] > maxLen:
                maxLen = dp[idx]
                # curr_idx = idx

        return maxLen                 