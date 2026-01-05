class Solution:
    def reverse(self, a, l, h):
        while l <= h:
            a[l], a[h] = a[h], a[l]
            l += 1
            h -= 1

    def nextPermutation(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(a)
        j = n-1

        while j > 0:
            if a[j-1] < a[j]:
                break
            j -= 1
        
        if j==0:
            self.reverse(a, 0, n-1)
            return 

        leftIdx = j
        pivot = a[j-1]
        j = n-1

        while j >= leftIdx and a[j] <= pivot:
            j -= 1
        
        a[leftIdx-1], a[j] = a[j], a[leftIdx-1]

        self.reverse(a, leftIdx, n-1)
        