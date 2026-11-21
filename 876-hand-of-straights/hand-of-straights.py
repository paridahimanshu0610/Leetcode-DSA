class Solution:
    def isNStraightHand(self, a: list[int], size: int) -> bool:
        n = len(a)
        if n % size != 0:
            return False

        a.sort()
        grps = []

        def findLower(aa, target):
            if len(aa)==0:
                return -1

            l, h = 0, len(aa)-1

            while l <= h:
                mid = (l+h)//2
                val, cnt = aa[mid]

                if val >= target:
                    h = mid-1
                else:
                    l = mid+1
            
            return h

        for i in range(n):
            idx = findLower(grps, a[i])
            if idx < 0:
                grps.append((a[i], 1))
            else:
                val, cnt = grps[idx]
                if (a[i] == val+1) and (cnt < size):
                    grps[idx] = (a[i], cnt+1)
                else:
                    grps.append((a[i], 1))

            # print(i, grps)
            # for j in range(len(grps)):
            #     val, cnt = grps[j]
            #     if a[i] == val+1 and cnt < size:
            #         grps[j] = (a[i], cnt+1)
            #         found = True
            #         break
            # if not found:
            #     grps.append((a[i], 1))
            
            if len(grps) > n//size:
                return False

        return True