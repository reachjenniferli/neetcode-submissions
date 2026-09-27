class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        end = 0
        setnums = set()
        output = 0

        for i in range(len(s)):
            if s[end] in setnums:
                
                while s[end] in setnums:
                    print(setnums)
                    setnums.remove(s[start])
                    start += 1
                    print(setnums)
            setnums.add(s[end])
            print(setnums)
            output = max(output, len(setnums))
            end += 1
            print(output)

        return output