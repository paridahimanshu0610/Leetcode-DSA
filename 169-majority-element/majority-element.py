class Solution:
    def majorityElement(self, a: List[int]) -> int:
        curr, currCnt = a[0], 0

        for e in a:
            if e == curr:
                currCnt += 1
            else:
                if currCnt == 0:
                    curr = e
                    currCnt = 1
                else:
                    currCnt -= 1

        return curr 