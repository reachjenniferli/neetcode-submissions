class Solution:
    def isValid(self, s: str) -> bool:
        
        ls = []
        
        for i in range(len(s)):
            print(ls)

            if s[i] == '(':
                ls.append('p')
            elif s[i] == '{':
                ls.append('c')
            elif s[i] == '[':
                ls.append('b')

            elif s[i] == ')':
                if len(ls) > 0 and ls[-1] == 'p':
                    ls.pop()
                else:
                    return False
            elif s[i] == '}':
                if len(ls) > 0 and ls[-1] == 'c':
                    ls.pop()
                else: 
                    return False
            elif s[i] == ']':
                if len(ls) > 0 and ls[-1] == 'b':
                    ls.pop()
                else: 
                    return False
        
        return len(ls) == 0

