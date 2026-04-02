class Solution:
    def getCount(self, a, target):
        if target < 0:
            return 0
            
        l, r = 0, 0
        res = 0
        curr_sum = 0

        while l<=r and r<len(a):
            curr_sum += a[r]
            if curr_sum <= target:
                res += (r-l+1)
            else:
                while l < r and curr_sum > target:
                    curr_sum -= a[l]
                    l += 1
                if l <= r and curr_sum == target:
                    res += (r-l+1)
            r += 1

        return res

    def numSubarraysWithSum(self, a: List[int], target: int) -> int:
        return self.getCount(a, target) - self.getCount(a, target-1)
                    