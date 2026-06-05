class Solution:
    def merge(self, a1: List[int], m: int, a2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = m

        i, j = 0, 0
        while i < m and j < n:
            if a1[i] < a2[j]:
                a1[idx % (m+n)] = a1[i]
                i += 1
            elif a1[i] > a2[j]:
                a1[idx % (m+n)] = a2[j]
                j += 1
            else:
                a1[idx % (m+n)] = a1[i]
                idx += 1
                a1[idx % (m+n)] = a2[j]
                i += 1
                j += 1
            idx += 1
        
        while i < m:
            a1[idx % (m+n)] = a1[i]
            idx += 1
            i += 1

        while j < n:
            a1[idx % (m+n)] = a2[j]
            idx += 1
            j += 1

        print(a1)

        for i in range(m//2):
            a1[i], a1[m-1-i] = a1[m-1-i], a1[i]
        
        print(a1)

        for j in range(n//2):
            i = m + j
            a1[i], a1[m+n-1-j] = a1[m+n-1-j], a1[i]

        print(a1)

        for i in range((m+n)//2):
            a1[i], a1[m+n-1-i] = a1[m+n-1-i], a1[i] 