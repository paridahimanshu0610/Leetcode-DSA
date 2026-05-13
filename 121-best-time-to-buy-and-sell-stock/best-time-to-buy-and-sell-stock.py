class Solution:
    def maxProfit(self, a: List[int]) -> int:
        curr_holding = a[0]
        res = 0

        for i in range(1, len(a)):
            if a[i] < curr_holding:
                curr_holding = a[i]
            
            res = max(res, a[i] - curr_holding)

        return res