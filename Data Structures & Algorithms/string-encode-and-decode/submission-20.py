class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s = (s + str(len(word)) + "#" + word)
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        word = ""
        res = []
        skips = 0
        number = ""

        for i in range(len(s)): 
            if skips == 0 and s[i]!="#":
                number += s[i]
            elif skips == 0 and s[i] == "#":
                skips = int(number)
                number = ""
                res.append(word)
                word = ""
            else:
                skips -= 1
                word += s[i]
        res.append(word)
        return res[1:]