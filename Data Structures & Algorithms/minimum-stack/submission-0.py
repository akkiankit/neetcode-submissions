class MinStack:

    def __init__(self):
        self.item = list()
        

    def push(self, val: int) -> None:
        return self.item.append(val)
        

    def pop(self) -> None:
        return self.item.pop()
        

    def top(self) -> int:
        return self.item[-1]
        

    def getMin(self) -> int:
        return min(self.item)
        
