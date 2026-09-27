class Solution:
    def isValid(self, s: str) -> bool:
        
        ls = []
        #closed = {')':'(', ']':'[', '}':'{'}
        
        for i in s:
            print(ls)

            if i == '(':
                ls.append('p')
            elif i == '{':
                ls.append('c')
            elif i == '[':
                ls.append('b')

            elif i == ')':
                if len(ls) > 0 and ls[-1] == 'p':
                    ls.pop()
                else:
                    return False
            elif i == '}':
                if len(ls) > 0 and ls[-1] == 'c':
                    ls.pop()
                else: 
                    return False
            elif i == ']':
                if len(ls) > 0 and ls[-1] == 'b':
                    ls.pop()
                else: 
                    return False
        
        return len(ls) == 0

