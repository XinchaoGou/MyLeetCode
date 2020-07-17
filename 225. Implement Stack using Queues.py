class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        q_length = len(self.q)
        while q_length > 1:
            self.q.append(self.q.pop(0))
            q_length -= 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not bool(self.q)

from collections import deque
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = deque()
        self.help = deque()
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.data) > 1:
            self.help.append(self.data.popleft())
        tmp = self.data.popleft()
        self.help,self.data = self.data,self.help
        return tmp
    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.data) != 1:
            self.help.append(self.data.popleft())
        tmp = self.data.popleft()
        self.help.append(tmp)
        self.help,self.data = self.data,self.help
        return tmp
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not bool(self.data)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()