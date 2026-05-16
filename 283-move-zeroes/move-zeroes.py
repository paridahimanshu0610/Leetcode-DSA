class Solution:
    def moveZeroes(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = 0
        i = 0

        while i < len(a):
            if a[i] != 0:
                a[ptr] = a[i]
                ptr += 1
            i += 1
        
        while ptr < len(a):
            a[ptr] = 0
            ptr += 1