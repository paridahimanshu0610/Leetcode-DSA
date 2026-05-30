from itertools import combinations
import bisect


class Solution:
    def minimumDifference(self, a: List[int]) -> int:
        def get_sums(arr):
            N = len(arr)
            ans = {}
            for k in range(1, N + 1):
                all_sums = set()
                for comb in combinations(arr, k):
                    all_sums.add(sum(comb))
                ans[k] = list(all_sums)

            return ans

        n = len(a) // 2
        lsums, rsums = get_sums(a[:n]), get_sums(a[n:])
        total = sum(a)
        half = total // 2
        minDiff = abs(sum(a[:n]) - sum(a[n:]))

        for k in range(1, n):
            curr_right_sums = rsums[n - k]
            curr_right_sums.sort()
            for left_sum in lsums[k]:
                right_target_sum = half - left_sum
                # p is the index of element just greater than or equal to right_target_sum
                p = bisect.bisect_left(curr_right_sums, right_target_sum)
                for q in [p, p - 1]:
                    if 0 <= q < len(curr_right_sums):
                        group1 = left_sum + curr_right_sums[q]
                        group2 = total - group1
                        minDiff = min(abs(group1 - group2), minDiff)

        return minDiff
