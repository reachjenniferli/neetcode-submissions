class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = 0
        self.minstack = []

    def push(self, val: int) -> None:
        if len(self.stack)>0:
            self.minimum = min(self.minstack[-1], val)
        else:
            self.minimum = val
        self.stack.append(val)
        self.minstack.append(self.minimum)

    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
