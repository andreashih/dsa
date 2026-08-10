# two queues
# Queue: FIFO
# Stack: LIFO
# 新的元素從右邊進來，再把前面的所有舊元素搬到它後面

from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque() # empty auxiliary queue

    def push(self, x: int) -> None:
        # Put the new element into the empty auxiliary queue
        self.q2.append(x)

        # Move all existing elements behind it
        while self.q1:
            self.q2.append(self.q1.popleft())

        # Swap the queues
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft() # 從左邊開始      

    def top(self) -> int:
        return self.q1[0] # 最左邊的

    def empty(self) -> bool:
        return not self.q1

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()