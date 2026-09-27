class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        permutation1 = {}
        permutation2 = {}

        for i in range(len(s1)):
            permutation1[s1[i]] = 1 + permutation1.get(s1[i], 0)
            permutation2[s2[i]] = 1 + permutation2.get(s2[i], 0)

        r = len(s1)

        #iterate through string
        for l in range(len(s2)-len(s1)+1):
            #print("permutation 1 " + str(permutation1))
            #print("permutation 2 " + str(permutation2))
            if permutation1 == permutation2:
                return True
            if permutation2[s2[l]] == 1:
                permutation2.pop(s2[l])
            else:
                permutation2[s2[l]] -= 1
            if r < len(s2):
                permutation2[s2[r]] = permutation2.get(s2[r], 0) + 1
            r += 1


        return False