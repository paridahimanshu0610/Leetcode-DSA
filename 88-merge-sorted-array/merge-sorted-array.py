class Solution:
    def merge(self, a1: List[int], m: int, a2: List[int], n: int) -> None:
        i = m - 1      # pointer for valid part of a1
        j = n - 1      # pointer for a2
        idx = m + n - 1  # pointer for write position (back of a1)

        while i >= 0 and j >= 0:
            if a1[i] >= a2[j]:
                a1[idx] = a1[i]
                i -= 1
            else:
                a1[idx] = a2[j]
                j -= 1
            idx -= 1

        # if a2 still has elements, copy them
        while j >= 0:
            a1[idx] = a2[j]
            idx -= 1
            j -= 1

        # if a1 still has elements, they're already in place