class Solution:

    def encode(self, strs: List[str]) -> str:
        single_string = ''
        for i in range(len(strs)):
            single_string += strs[i] + "¥" 
        #print(single_string)
        return single_string

    def decode(self, s: str) -> List[str]:
        strs = []
        word = ''
        for i in s:
            if i == '¥':
                strs.append(word)
                word = ''

            else:
                word += i
                #print(word)
        return strs
