class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum = min(val, self.minimum)
        self.minstack.append(self.minimum)
        print('______')
        print(self.stack)
        print(self.minstack)

    def pop(self) -> None:
        self.stack.pop()
        if len(self.minstack) > 1: self.minimum = self.minstack[-2]
        else: self.minimum = float('inf')
        self.minstack.pop()
        print('______')
        print(self.stack)
        print(self.minstack)
        

    def top(self) -> int:
        return self.stack[-1]
        print('______')
        print(self.stack)
        print(self.minstack)
        

    def getMin(self) -> int:
        return self.minstack[-1]
        print('______')
        print(self.stack)
        print(self.minstack)

        
