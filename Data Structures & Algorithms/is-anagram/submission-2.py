class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dictS = dict()

        for x in s:
            if x not in dictS:
                dictS[x] = 1
            else:
                dictS[x] += 1
        
        for x in t:
            if x not in dictS:
                return False
            else:
                dictS[x] -= 1
            if dictS[x] == 0:
                dictS.pop(x)
         
        if not dictS:
            return True
        else:
            return False