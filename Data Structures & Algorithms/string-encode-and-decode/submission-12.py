class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encoded = ""
        
        for n in strs:
            encoded = encoded + n
            encoded += ":?"

        return str(encoded)

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, s:str):
        #original = s.split(":?")
        #original.pop()

        if s == ":?":
            return [""]

        original = []
        word = ""
        i = 0
        
        while(i < (len(s))):

            if s[i] == ":" and s[i+1] == "?":
                original.append("")
                word = ""
                i += 2

            word += s[i]

            if s[i+1] == ":":
                if s[i+2] == "?":
                    original.append(str(word))
                    word = ""
                    i += 2
            
            i += 1
            

        return original