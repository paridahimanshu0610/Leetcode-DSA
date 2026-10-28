class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        count = {5:0, 10:0, 20:0}

        for bill in bills:
            count[bill] += 1
            left = bill-5

            cnt20 = min(left//20, count[20])
            left -= cnt20*20
            count[20] -= cnt20
            # cnt20 = left//20 
            # if cnt20 > count[20]:
            #     left = left - count[20]*20
            #     count[20] = 0
            # else:
            #     left = left - cnt20*20
            #     count[20] -= cnt20

            cnt10 = min(left//10, count[10])
            left -= cnt10*10
            count[10] -= cnt10
            # cnt10 = left//10
            # if cnt10 > count[10]:
            #     left = left - count[10]*10
            #     count[10] = 0
            # else:
            #     left = left - cnt10*10
            #     count[10] -= cnt10

            cnt5 = min(left//5, count[5])
            left -= cnt5*5
            count[5] -= cnt5
            # cnt5 = left//5
            # if cnt5 > count[5]:
            #     left = left - count[5]*5
            #     count[5] = 0
            # else:
            #     left = left - cnt5*5
            #     count[5] -= cnt5

            if left > 0:
                return False

        return True