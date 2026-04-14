class Solution:
    def checkSubarraySum(self, a: List[int], k: int) -> bool:
        remainder_idx = {0:-1}
        curr_sum = 0

        for i in range(len(a)):
            curr_sum += a[i]
            temp = curr_sum % k
            # print(i, curr_sum, temp, remainder_idx)

            if temp in remainder_idx:
                if (i-remainder_idx[temp]) > 1:
                    return True
            else:
                remainder_idx[temp] = i
        
        return False