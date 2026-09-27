class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i, n in enumerate(tokens):
            if n == "+":
                stack[-2] += stack[-1]
                stack.pop()                   
            elif n == "-":
                stack[-2] -= stack[-1]
                stack.pop()      
            elif n == "*":
                stack[-2] *= stack[-1]
                stack.pop()
            elif n == "/":
                stack[-2] /= stack[-1]
                stack.pop()
                stack[-1] = int(stack[-1])
            else:
                stack.append(int(n))
        return stack[0]
                
                
                