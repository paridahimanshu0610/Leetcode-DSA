class Solution:
    def mergeSort(self, a, l, h, currCnt, temp):
        if (h-l+1) == 1:
            return currCnt
        
        mid = (l+h)//2
        currCnt = self.mergeSort(a, l, mid, currCnt, temp)
        currCnt = self.mergeSort(a, mid+1, h, currCnt, temp)

        j = mid+1
        for i in range(l, mid+1):
            while j <= h and a[i] > 2*a[j]:
                j += 1
            currCnt += (j - (mid+1))

        i, j, k = l, mid+1, 0
        while i <= mid and j <= h:
            if a[i] <= a[j]:
                temp[l+k] = a[i]
                i += 1
            else:
                temp[l+k] = a[j]
                j += 1
            k += 1

        while i <= mid:
            temp[l+k] = a[i]
            i += 1
            k += 1
        
        while j <= h:
            temp[l+k] = a[j]
            j += 1
            k += 1

        for i in range(l, h+1):
            a[i] = temp[i]

        return currCnt

    def reversePairs(self, a: List[int]) -> int:
        temp = [None]*len(a)
        return self.mergeSort(a, 0, len(a)-1, 0, temp)    