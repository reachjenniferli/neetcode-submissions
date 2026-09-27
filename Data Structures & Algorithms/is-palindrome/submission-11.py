class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        i = 0
        a = len(s)-1

        while a > i:
            while not s[i].isalnum() and i < len(s)-1:
                i += 1
            while not s[a].isalnum() and a > -1:
                a -= 1
            if s[i] != s[a]:
                return False
            i += 1
            a -= 1
        
        return True

