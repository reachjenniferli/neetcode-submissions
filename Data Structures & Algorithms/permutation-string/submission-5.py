class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1dict = 26*[0]
        s2dict = 26*[0]

        for i in range(len(s1)):
            s1dict[ord(s1[i])-ord('a')] += 1
        
        for i in range(len(s1)):
            print("s1dict")
            print(s1dict)
            print("s2dict")
            print(s2dict)
            
            s2dict[ord(s2[i])-ord('a')] += 1
            if s2dict == s1dict:
                return True
        
        L = 0
        R = len(s1)
        
        while R < len(s2):
            print("s1dict")
            print(s1dict)
            print("s2dict")
            print(s2dict)
            
            if s2dict == s1dict:
                return True

            s2dict[ord(s2[R])-ord('a')] += 1
            R += 1
            
            s2dict[ord(s2[L])-ord('a')] -= 1
            L += 1
        
        if s2dict == s1dict:
                return True
        print("s1dict")
        print(s1dict)
        print("s2dict")
        print(s2dict)
        
        return False