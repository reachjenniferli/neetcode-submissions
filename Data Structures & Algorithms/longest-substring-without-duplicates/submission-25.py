class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        if not s:
            return 0

        left = 0
        right = 0
        length = 1

        for right in range(len(s)):
            if s[right] in characters:
                length = max(len(characters), length)
                while s[left] != s[right]:
                    characters.remove(s[left])
                    left += 1
                characters.remove(s[left])
                left += 1
            characters.add(s[right])
                
        length = max(len(characters), length)
        return length
