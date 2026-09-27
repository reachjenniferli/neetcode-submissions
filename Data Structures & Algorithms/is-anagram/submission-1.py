class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = dict()
        dictT = dict()

        for x in s:
            if x not in dictS:
                dictS[x] = 1
            else:
                dictS[x] += 1
        
        for x in t:
            if x not in dictT:
                dictT[x] = 1
            else:
                dictT[x] += 1
        
        if dictS == dictT:
            return True
        else:
            return False