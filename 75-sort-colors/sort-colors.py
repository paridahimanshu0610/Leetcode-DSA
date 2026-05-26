class Solution:
    def sortColors(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(a)
        p1, p2 = 0, n-1

        i = 0

        while i <= p2:
            if a[i] == 0:
                a[p1] = 0
                p1 += 1
            elif a[i] == 2:
                while p2 > i and a[p2] == 2:
                    p2 -= 1
                if a[p2] == 0:
                    a[p1] = 0
                    p1 += 1
                a[p2] = 2
                p2 -= 1

            i += 1

        while p1 <= p2:
            a[p1] = 1
            p1 += 1   