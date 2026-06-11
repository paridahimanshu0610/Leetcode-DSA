class Solution:
    def maxProduct(self, a: List[int]) -> int:
        res, currMax, currMin = a[0], a[0], a[0]

        for e in a[1:]:
            if e >= 0:
                currMax, currMin = max(e, e*currMax), min(e, e*currMin)
            else:
                currMax, currMin = max(e, e*currMin), min(e, e*currMax)
            
            res = max(res, currMax)

        return res