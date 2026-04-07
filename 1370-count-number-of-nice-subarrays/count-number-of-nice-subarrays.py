class Solution:
    def count(self, a, k):
        l, r = 0, 0
        res = 0
        curr_sum = 0

        while l <= r and r < len(a):
            if a[r]%2==1:
                curr_sum += 1
            
            while l < r and curr_sum > k:
                if a[l]%2==1:
                    curr_sum -= 1
                l += 1
            
            if curr_sum <= k:
                res += (r-l+1)

            r += 1

        return res

    def numberOfSubarrays(self, a: List[int], k: int) -> int:
        res1 = self.count(a, k)
        res2 = self.count(a, k-1)
        # print(res1, res2)
        return res1 - res2