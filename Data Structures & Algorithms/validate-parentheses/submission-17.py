class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i, n in enumerate(s):
            if n == ']':
                if len(stack) == 0 or stack.pop() != "[":
                    return False
            elif n == ')':
                if len(stack) == 0 or stack.pop() != "(":
                    return False
            elif n == '}':
                if len(stack) == 0 or stack.pop() != "{":
                    return False

            else:
                stack.append(n)

        if len(stack) == 0:
            return True
        else:
            return False