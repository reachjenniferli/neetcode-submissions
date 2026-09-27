class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        permutation = sorted(s1)
        l = 0
        r = len(s1)

        #iterate through string
        while r <= len(s2):
            substring = sorted(s2[l:r])
            print(r)
            print("substring " + str(substring))
            print("permutation " + str(permutation))
            if str(substring) == str(permutation):
                return True
            l += 1
            r += 1

        return False



                