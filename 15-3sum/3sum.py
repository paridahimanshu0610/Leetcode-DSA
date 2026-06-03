class Solution:
    def threeSum(self, a: list[int]) -> list[list[int]]:
        a.sort()

        n = len(a)
        i = 0
        j, k = 1, n-1
        res = []
        target = 0

        while i < n-2:
            if i > 0 and a[i] == a[i-1]:
                i += 1
                continue
            
            j, k = i+1, n-1
            while j < k and j < n-1 and k < n:
                currSum = a[i] + a[j] + a[k]

                if currSum > target:
                    k -= 1
                elif currSum < target:
                    j += 1
                else:
                    res.append([a[i], a[j], a[k]])
                    currLeft, currRight = a[j], a[k]

                    while a[j] == currLeft and j < k:
                        j += 1
                    
                    while a[k] == currRight and k > j:
                        k -= 1
            
            i += 1
        
        return res