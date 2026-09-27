class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        if not s:
            return 0

        left = 0
        right = 0
        length = 1

        while right < len(s) and left <= right:
            if s[right] in characters:
                length = max(len(characters), length)
                while s[left] != s[right]:
                    characters.remove(s[left])
                    left += 1
                characters.remove(s[left])
                left += 1
            else:
                characters.add(s[right])
                right += 1
            print(characters)
                
        length = max(len(characters), length)
        return length
