class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        sign = 1

        if ((dividend < 0) and (divisor > 0)) or ((dividend > 0) and (divisor < 0)) :
            sign = -1
        divisor, dividend = abs(divisor), abs(dividend) 
        while dividend >= divisor:
            shift = 1
            while dividend >= divisor << shift:
                shift += 1
            shift -= 1
            res += 1 << shift
            if res == 1<<31 and sign > 0:
                return (1<<31) - 1
            elif res == 1<<31 and sign < 0:
                return -1<<31

            dividend -= divisor << shift
        
        return sign*res