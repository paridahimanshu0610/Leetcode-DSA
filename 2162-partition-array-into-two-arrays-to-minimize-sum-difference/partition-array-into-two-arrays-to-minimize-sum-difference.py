from itertools import combinations
import bisect

class Solution:
    def getCombinations(self, a):
        n = len(a)
        res = {}

        for k in range(1, n+1):
            all_sum_set = set()
            for comb in combinations(a, k):
                all_sum_set.add(sum(comb))
            res[k] = list(all_sum_set)

        return res

    def minimumDifference(self, a: List[int]) -> int:
        n = len(a) // 2
        total = sum(a)
        target = total // 2

        left_sums, right_sums = self.getCombinations(a[:n]), self.getCombinations(a[n:])
        minDiff = abs(sum(a[:n])-sum(a[n:]))

        for k in range(1, n):
            curr_right_sums = right_sums[n-k]
            curr_right_sums.sort()
            for curr_left_sum in left_sums[k]:
                right_sum_target = target - curr_left_sum 
                # Retrieving the position index of the element just greater than right_sum_target
                p = bisect.bisect_left(curr_right_sums, right_sum_target)
                for q in [p-1, p]:
                    if 0 <= q < len(curr_right_sums):
                        curr_right_sum = curr_right_sums[q]
                        curr_total = curr_left_sum + curr_right_sum
                        minDiff = min(minDiff, abs(curr_total - (total-curr_total)))

        return minDiff