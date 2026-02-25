class Solution:
    def hammingWeight(self, n: int) -> int:
        curr = n
        res = 1
        while curr != 1:
            if curr%2==1:
                res += 1
            curr = curr//2

        return res