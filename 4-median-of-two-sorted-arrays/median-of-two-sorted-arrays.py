class Solution:
    def findMedianSortedArrays(self, a1: List[int], a2: List[int]) -> float:
        n, m = len(a1), len(a2)
        if n > m:
            return self.findMedianSortedArrays(a2, a1)

        lhs = (n+m+1)//2  # Number of elements that must be on the LHS

        l, h = 0, min(n, lhs)

        while l <= h:
            mid1 = (l+h)//2
            mid2 = lhs-mid1

            l1 = a1[mid1-1] if mid1 >= 1 else float("-inf")
            l2 = a2[mid2-1] if mid2 >= 1 else float("-inf")

            r1 = a1[mid1] if mid1 < n else float("inf")
            r2 = a2[mid2] if mid2 < m else float("inf")

            if l1 > r2:
                h = mid1-1
            elif l2 > r1:
                l = mid1+1
            else:
                break

        if (n+m)%2 == 0:
            return (max(l1,l2) + min(r1, r2))/2
        else:
            return max(l1, l2)