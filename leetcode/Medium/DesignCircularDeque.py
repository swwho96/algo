class MyCircularDeque:

    def __init__(self, k: int):
        self.k, self.len = k, 0
        self.data = []

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.data = [value] + self.data
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.data.append(value)
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.data.pop(0)
            return True
            
        
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.data.pop()
            return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.data[0]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.data[-1]
        

    def isEmpty(self) -> bool:
        return True if len(self.data) == 0 else False
        

    def isFull(self) -> bool:
        return True if len(self.data) == self.k else False