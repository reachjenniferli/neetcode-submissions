class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        if k >= len(s)-1:
            return len(s)
        
        letters = {s[0]: 1}
        l = 0
        r = 0
        res = 0

        while r < len(s): 

            #find most common letter
            most_freq = max(letters.values())
            total = sum(letters.values())
            print(s[l:r+1])
            print("letters: " + str(letters))
            print("most freq: " + str(most_freq))
            print("total: " + str(total))

            #check if valid
            if (total - most_freq) <= k:
                r += 1
                res = max(res, total)
                #add to dict
                if r < len(s):
                    letters[s[r]] = letters.get(s[r], 0) + 1

            else: 
                #remove from dict
                letters[s[l]] = letters.get(s[l], 0) - 1
                l += 1


        return res