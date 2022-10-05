class MinStack:

    def __init__(self):
        # the init function calls the other functions
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)
        

    def pop(self) -> None:
        # void pop() removes the element on the top of the stack.
        # specify which indice, 0, to remove from the stack
        
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        # when they say top element of the stack, do they mean the last element?
        # gets the last element of the stack
        
        # loop to return the last element, the negative 1 index
        
        return self.stack[-1]
        

    def getMin(self) -> int:
        
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
