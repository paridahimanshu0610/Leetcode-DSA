class Solution:
    def mergeTriplets(self, a: list[list[int]], tgt: list[int]) -> bool:
        merged = [float("-inf"), float("-inf"), float("-inf")]

        for curr in a:
            if (curr[0]<=tgt[0]) and (curr[1]<=tgt[1]) and (curr[2]<=tgt[2]):
                for i in range(len(merged)):
                    merged[i] = max(merged[i], curr[i])
            
        return merged == tgt