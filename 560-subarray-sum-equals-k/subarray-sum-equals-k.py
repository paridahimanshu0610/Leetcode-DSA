class Solution:
    def subarraySum(self, a: List[int], k: int) -> int:
        sum_freq = {0:1}
        sum_so_far, res = 0, 0

        for i in range(len(a)):
            sum_so_far += a[i]
            res += sum_freq.get(sum_so_far-k, 0)
            sum_freq[sum_so_far] = sum_freq.get(sum_so_far, 0)+1
        
        return res