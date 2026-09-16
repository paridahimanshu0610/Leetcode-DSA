class StockSpanner:
    def __init__(self):       
        self.stack = []

    def next(self, price: int) -> int:  
        total_cnt = 1
        while len(self.stack) > 0 and price >= self.stack[-1][0]:
            _, cnt = self.stack.pop()
            total_cnt += cnt

        self.stack.append((price, total_cnt))

        return total_cnt     

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)