class Solution:
    def update_set(self, item, curr_set_freq):
        curr_set_freq[item] = 1 if item not in curr_set_freq else curr_set_freq[item]+1

    def totalFruit(self, a: List[int]) -> int:
        res = 1
        curr_set_freq = {a[0]:1}
        start, end = 0, 0

        while start <= end and end < len(a):
            if len(curr_set_freq) > 2:
                curr_set_freq[a[start]]-=1
                if curr_set_freq[a[start]]==0:
                    del curr_set_freq[a[start]]
                start += 1
            else:
                res = max(res, end-start+1)
            end += 1
            if end < len(a):
                self.update_set(a[end], curr_set_freq)

        return res




