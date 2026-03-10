import math
class Solution:
    def countPrimes(self, n: int) -> int:
        prime_status = [1]*(n-2)

        for i in range(2, math.ceil(math.sqrt(n))):
            if prime_status[i-2] == 1:
                # Mark all multiples of curr_prime as 0
                for j in range(i*i, n, i):
                    prime_status[j-2] = 0
        
        return sum(prime_status)