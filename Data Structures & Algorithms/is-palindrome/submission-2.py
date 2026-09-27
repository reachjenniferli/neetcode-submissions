class Solution:
    def isPalindrome(self, s: str) -> bool:
        end = len(s)

        s = s.lower()
        for i in s:
            if i.isalnum():
                continue
            if ord(i) < 97 or ord(i) > 122:
                s = s.replace(i, '')
        print(s)

        for i in range(len(s)//2):
            if s[i] != s[len(s) - 1 - i]:
                print(s[i])
                print(s[len(s)- 1 - i])
                return False
        return True
        