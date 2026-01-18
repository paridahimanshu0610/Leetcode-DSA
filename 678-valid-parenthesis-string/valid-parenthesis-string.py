class Solution:
    def checkValidString(self, s: str) -> bool:
        min_cnt, max_cnt = 0, 0

        for c in s:
            if c=="(":
                min_cnt+=1
                max_cnt+=1
            elif c==")":
                min_cnt-=1
                if min_cnt < 0 and max_cnt > 0:
                    min_cnt = 0
                max_cnt-=1
            else:
                min_cnt = max(0, min_cnt-1)
                max_cnt+=1
            
            
            if min_cnt < 0 and max_cnt < 0:
                return False
        
        return 0==min_cnt