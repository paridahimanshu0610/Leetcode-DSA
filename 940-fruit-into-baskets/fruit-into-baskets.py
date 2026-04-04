class Solution:
    def totalFruit(self, a: List[int]) -> int:
        freq = {}
        l, r = 0, 0
        res = 0

        while l <= r and r < len(a):
            freq[a[r]] = freq.get(a[r], 0) + 1

            while len(freq) > 2 and l < r:
                freq[a[l]] -= 1
                if freq[a[l]]==0:
                    del freq[a[l]]
                l += 1
            
            res = max(res, r-l+1)
            r += 1

        return res