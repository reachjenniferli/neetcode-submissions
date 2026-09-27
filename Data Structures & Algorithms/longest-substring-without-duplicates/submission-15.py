class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window (two pointers)
        charSet = set() #set because checking if r is in set is O(1)
        l = 0 #left pointer
        res = 0 #length of longest substring

        for r in range(len(s)):
            while s[r] in charSet: #while duplicate is in our substring
                charSet.remove(s[l]) #remove letters from beginning of substring
                l += 1 #until dupe is gone, close sliding window from left
            charSet.add(s[r]) #else, add element to substring
            res = max(res, r - l + 1) #update longest substring length
         
        return res #return length of longest substring