class Solution:
    def encode(self, strs: List[str]) -> str:
        
        encoded = ""
        
        for n in strs:
            encoded = encoded + n
            encoded += ":?"

        return str(encoded)

    def decode(self, s: str) -> List[str]:

        original = s.split(":?")
        original.pop()
        #word = ""
        
        #for i in range(len(s) - 2):

        #    word += s[i]

        #    if s[i+1] == ":":
        #        if s[i+2] == ":":
        #            original.append(str(word))
        #            word = ""
            

        return original