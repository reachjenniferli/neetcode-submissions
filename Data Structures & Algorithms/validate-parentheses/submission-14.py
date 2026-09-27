class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 

        for i in range(len(s)):
            curr = s[i]
            if curr == '(' or curr == '{' or curr == '[':
                stack.append(curr)
            else:
                if not stack:
                    return False
                elif curr == ')' and stack[-1] != '(':
                    return False
                elif curr == '}' and stack[-1] != '{':
                    return False
                elif curr == ']' and stack[-1] != '[':
                    return False
                else:
                    stack.pop()

        if not stack:
            return True
        else:
            return False