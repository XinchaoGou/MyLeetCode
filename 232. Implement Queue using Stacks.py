class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mQueue_1 = []
        self.mQueue_2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        for i in range(len(self.mQueue_1)):
            self.mQueue_2.append(self.mQueue_1.pop())
        self.mQueue_1.append(x)
        for i in range(len(self.mQueue_2)):
            self.mQueue_1.append(self.mQueue_2.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.mQueue_1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.mQueue_1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.mQueue_1) == 0


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.peek()
param_3 = obj.pop()
param_4 = obj.empty()

print(param_2, param_3, param_4)
