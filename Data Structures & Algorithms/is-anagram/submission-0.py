class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        string_list = []
        for i in range (len(t)):
            string_list.append(t[i])
        for i in range (len(s)):
            if s[i] not in string_list:
                return False
            string_list.remove(s[i])
        return True
        