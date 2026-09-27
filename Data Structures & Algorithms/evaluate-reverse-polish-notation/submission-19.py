class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        total = int()

        for i, token in enumerate(tokens):
            
            if token == '+' or token == '-' or token == '*' or token == '/':
                if token == '+':
                    stack[-2] += stack[-1]
                    stack.pop()
                if token == '-':
                    stack[-2] -= stack[-1]
                    stack.pop()
                if token == '*':
                    stack[-2] *= stack[-1]
                    stack.pop()
                if token == '/':
                    stack[-2] = int(stack[-2] / stack[-1])
                    stack.pop()
                    
                #stack.append(total)
            else: 
                stack.append(int(token))
                    
                    
            print(stack)
            print(token)
            print('_____')

        return (int(stack[0]))
