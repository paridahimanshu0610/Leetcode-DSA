from collections import deque

class MyQueue:

    def __init__(self):
        self.stack1 = deque() # Main stack
        self.stack2 = deque() # Auxilliary stack

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1

        while len(self.stack1)!=1:
            self.stack2.append(self.stack1.pop())

        val = self.stack1.pop() # At this point, stack1 becomes empty

        while len(self.stack2)!=0:
            self.stack1.append(self.stack2.pop())

        return val

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        return len(self.stack1)==0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()