class Solution:
    def majorityElement(self, a: List[int]) -> int:
        max_e, cnt = a[0], 1
        for i in range(1, len(a)):
            if a[i]==max_e:
                cnt+=1
            else:
                cnt -= 1
                if cnt==0:
                    max_e = a[i]
                    cnt = 1
        
        return max_e