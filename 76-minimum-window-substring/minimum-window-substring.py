class Solution:
    def check(self, freq, c):
        if c in freq:
            freq[c] -= 1
            if freq[c] == 0:
                del freq[c]

        return len(freq)==0
        
    def minWindow(self, s: str, t: str) -> str:
        tf = {}
        res = s

        for c in t:
            tf[c] = tf.get(c, 0) + 1
        
        l, r  = 0, 0
        cnt = 0
        flag = False

        temp = tf.copy()
        while l <= r and r < len(s):
            if temp.get(s[r], 0) > 0:
                cnt += 1
            temp[s[r]] = temp.get(s[r], 0) - 1

            while cnt == len(t):
                flag = True
                res = s[l:r+1] if (r-l+1) < len(res) else res
                temp[s[l]] += 1
                if temp[s[l]] > 0:
                    cnt -= 1
                l += 1

            r += 1


        return res if flag else ""