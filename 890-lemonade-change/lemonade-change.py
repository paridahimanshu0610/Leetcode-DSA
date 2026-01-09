class Solution:
    def lemonadeChange(self, a: List[int]) -> bool:
        change = {5:0, 10:0}

        for i in range(len(a)):
            if a[i]==5:
                change[5]+=1
            elif a[i]==10:
                change[5]-=1
                change[10]+=1
            else:
                if change[10]==0:
                    change[5]-=3
                else:
                    change[5]-=1
                    change[10]-=1
            
            if change[5]<0 or change[10]<0:
                return False

        return True
