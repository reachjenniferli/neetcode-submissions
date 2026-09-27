class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s = (s + word + "#@$%!")
        return s

    def decode(self, s: str) -> List[str]:
        strs = s.split("#@$%!")
        return strs[0:-1]