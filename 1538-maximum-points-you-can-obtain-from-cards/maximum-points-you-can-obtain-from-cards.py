class Solution:
    def maxScore(self, a: List[int], k: int) -> int:
        min_curr_sum, curr_sum, total_sum = float('inf'), 0, 0

        for i in range(len(a)-k):
            curr_sum += a[i]
        
        total_sum = curr_sum
        min_curr_sum = curr_sum  
        l, r = 0, len(a)-k

        while r < len(a):
            curr_sum -= a[l]
            curr_sum += a[r]
            total_sum += a[r]

            min_curr_sum = min(min_curr_sum, curr_sum)

            l += 1
            r += 1

        return total_sum - min_curr_sum