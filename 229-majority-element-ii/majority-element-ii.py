class Solution:
    def majorityElement(self, a: List[int]) -> List[int]:
        cand1, cand2 = None, None
        cnt1, cnt2 = 0, 0

        for e in a:
            if cnt1 == 0 and e != cand2:
                cand1 = e
                cnt1 = 1
            elif cnt2 == 0 and e != cand1:
                cand2 = e
                cnt2 = 1
            elif e == cand1:
                cnt1 += 1
            elif e == cand2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1, cnt2 = 0, 0
        res = []

        for e in a:
            if e == cand1:
                cnt1 += 1
            elif e == cand2:
                cnt2 += 1
        
        if cnt1 > len(a)//3:
            res.append(cand1)
            
        if cnt2 > len(a)//3:
            res.append(cand2)

        return res