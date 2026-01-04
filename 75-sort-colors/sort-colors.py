class Solution:
    def sortColors(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx0, idx1, idx2 = 0, 0, len(a)-1

        while idx1 <= idx2:
            if a[idx1]==0:
                a[idx1], a[idx0] = a[idx0], a[idx1]
                idx1+=1
                idx0+=1
            elif a[idx1]==2:
                a[idx2], a[idx1] = a[idx1], a[idx2]
                idx2-=1
            else:
                idx1+=1
