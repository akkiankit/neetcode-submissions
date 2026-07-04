class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

    # def __init__(self):
    #     self.item = list()
        

    # def push(self, val: int) -> None:
    #     return self.item.append(val)
        

    # def pop(self) -> None:
    #     return self.item.pop()
        

    # def top(self) -> int:
    #     return self.item[-1]
        

    # def getMin(self) -> int:
    #     return min(self.item)
        
