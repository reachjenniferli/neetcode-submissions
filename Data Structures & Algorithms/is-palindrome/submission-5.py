class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()

        lowercase = ""

        for n in s:
            if n.isalnum():
                    lowercase += n
        
        if lowercase != lowercase[::-1]:
                return False

        return True

