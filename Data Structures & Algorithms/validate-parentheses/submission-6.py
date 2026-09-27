class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = []
        for i in s:
            print(parentheses)
            print(i)
            if i == '(' or i == '[' or i == '{':
                parentheses.append(i)
            elif i == ')':
                if len(parentheses) == 0 or parentheses[-1] != '(':
                    return False
                parentheses.pop()
            elif i == ']':
                if len(parentheses) == 0 or parentheses[-1] != '[':
                    return False
                parentheses.pop()
            elif i == '}':
                if len(parentheses) == 0 or parentheses[-1] != '{':
                    return False
                parentheses.pop()
        if len(parentheses) != 0:
            return False
        return True
