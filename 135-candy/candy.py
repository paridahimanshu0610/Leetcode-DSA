class Solution:
    def candy(self, a: list[int]) -> int:
        n = len(a)
        left = [1]*n
        right = [1]*n
        res = 0

        for i in range(1, n):
            if a[i] > a[i-1]:
                left[i] += left[i-1]

        res = max(left[n-1], right[n-1])

        for i in range(n-2, -1, -1):
            if a[i] > a[i+1]:
                right[i] += right[i+1]

            res += max(left[i], right[i])
        
        return res