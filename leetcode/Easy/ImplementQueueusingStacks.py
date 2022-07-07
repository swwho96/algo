'''
Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
'''

class MyQueue:

    def __init__(self):
        self.myq = []

    def push(self, x: int) -> None:
        self.myq.append(x)

    def pop(self) -> int:
        return self.myq.pop(0)

    def peek(self) -> int:
        if len(self.myq) > 0:
            return self.myq[0]
        else:
            return null

    def empty(self) -> bool:
        return False if self.myq else True
