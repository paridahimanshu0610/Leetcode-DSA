class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        ends0, ends1 = 0, 0
        hasZero = 0

        for c in binary:
            if c == "1":
                ends1 = (ends1 + ends0 + 1) % (1e9 + 7)
            else:
                hasZero = 1
                ends0 = (ends1 + ends0) % (1e9 + 7)


        return int((ends0 + ends1 + hasZero) % (1e9 + 7))