class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s = (s + word + "#@$")
        return s

    def decode(self, s: str) -> List[str]:
        word = ""
        res = []
        skips = 0

        for i in range(len(s)): 
            if skips > 0:
                skips -= 1
                continue
            if s[i] == "#" and s[i+1] == "@" and s[i+2] == "$":
                res.append(word)
                word = ""
                skips = 2
                continue
            else:
                word += s[i]
        return res