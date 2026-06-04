class Solution:
    def fourSum(self, a: List[int], target: int) -> List[List[int]]:
        if len(a) < 4:
            return []
        
        a.sort()
        n = len(a)
        res = []
        i = 0

        while i < n-3:
            if i > 0 and a[i] == a[i-1]:
                i += 1
                continue
            j = i+1
            while j < n-2:
                if j > i+1 and a[j] == a[j-1]:
                    j += 1
                    continue
                
                p, q = j+1, n-1
                
                while p < q and p < n-1 and q < n:
                    currSum = a[i] + a[j] + a[p] + a[q]

                    if currSum > target:
                        q -= 1
                    elif currSum < target:
                        p += 1
                    else:
                        res.append([a[i], a[j], a[p], a[q]])
                        currLeft, currRight = a[p], a[q]

                        while a[p] == currLeft and p < q:
                            p += 1
                        
                        while a[q] == currRight and p < q:
                            q -= 1
                
                j += 1
            
            i += 1

        return res