class Solution:
    def maxSubarraySumCircular(self, a: list[int]) -> int:
        n = len(a)
        maxSum, minSum = -float("inf"), float("inf")
        prevMaxSum, prevMinSum, total = 0, 0, 0

        for i in range(n):
            if prevMaxSum + a[i] > a[i]:
                prevMaxSum = prevMaxSum+a[i]
            else:
                prevMaxSum = a[i]
            
            if prevMinSum + a[i] < a[i]:
                prevMinSum = prevMinSum+a[i]
            else:
                prevMinSum = a[i]            
                
            maxSum = max(maxSum, prevMaxSum)
            minSum = min(minSum, prevMinSum)

            total += a[i]
        
        # maxSum will only be negative when all terms are negative 
        return max(maxSum, total-minSum) if maxSum > 0 else maxSum