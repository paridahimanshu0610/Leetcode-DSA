class Solution:
    def reverse(self, a, start, end):
        k = 0
        for ii in range(start, (start+end+1)//2):
            a[ii], a[end-k] = a[end-k], a[ii]
            k += 1 

    def nextPermutation(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(a)
        if n == 1:
            return

        i, j = n-2, n-1

        while i >= 0 and j >= 0 and a[i] >= a[j]:
            i -= 1
            j -= 1

        if i < 0:
            self.reverse(a, 0, n-1)
            return 

        ii = n-1
        while ii > j:
            if a[ii] > a[i]:
                break
            ii -= 1

        a[i], a[ii] = a[ii], a[i]

        self.reverse(a, j, n-1)