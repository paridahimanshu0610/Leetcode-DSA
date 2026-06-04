class Solution:
    def fourSum(self, a: List[int], target: int) -> List[List[int]]:
        res = set()
        n = len(a)

        for i in range(n-3):
            for j in range(i+1, n-2):
                visited = set()
                for k in range(j+1, n):
                    required = target - (a[i]+a[j]+a[k])
                    if required in visited:
                        res.add(tuple(sorted([a[i], a[j], a[k], required])))
                    visited.add(a[k])

        return [list(temp) for temp in res]