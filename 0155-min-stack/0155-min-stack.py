class MinStack:

    def __init__(self):
        self.items = []
        self.minu = []

    def push(self, value: int) -> None:
        if len(self.items)==0:
            self.items.append(value)
            self.minu.append(value)
        else:
            self.items.append(value)
            self.minu.append(min(value,self.minu[-1]))

        

    def pop(self) -> None:
        if len(self.items)!=0:
            self.minu.pop()
            return self.items.pop()
        return null
            
        

    def top(self) -> int:
        if len(self.items)!=0:
            return self.items[-1]
        return null
        

    def getMin(self) -> int:
        if len(self.items)!=0:
            return self.minu[-1]
        return null
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()