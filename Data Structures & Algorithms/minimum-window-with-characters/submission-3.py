class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        longstr = {}
        shortstr = {}
        l = 0
        r = 0
        correct = 0
        substring = [0, 1001] #record l and r

        for i in range(len(t)):
            shortstr[t[i]] = shortstr.get(t[i], 0) + 1

        if s[0] in shortstr:
            longstr[s[r]] = longstr.get(s[r], 0) + 1
            #if number of r elements is correct
            if longstr.get(s[r]) and longstr.get(s[r]) == shortstr.get(s[r]):
                correct += 1

        while l < (len(s) - len(t)+1):
            #get rid of hanging letters at beginning
            while s[l] not in shortstr and l < r:
                l += 1

            print(s[l:r+1])
            print(correct)
            print(str(longstr))
            print("___")

            #if longstr is overshot and its on the left side
            if longstr.get(s[l]) and longstr.get(s[l]) > shortstr.get(s[l]):
                longstr[s[l]] = longstr.get(s[l], 0) - 1
                l += 1
                
            #if correct is less than its supposed to then increment r and add if in shortstr
            if correct < len(set(t)) and r < len(s)-1:
                r += 1
                #incrementing longstr if present
                if s[r] in shortstr:
                    longstr[s[r]] = longstr.get(s[r], 0) + 1
                    #if number of r elements is correct
                    if longstr.get(s[r]) and longstr.get(s[r]) == shortstr.get(s[r]):
                        correct += 1

            elif correct == len(set(t)):
                if (r - l) < (substring[-1] - substring[-2]):
                    substring.append(l)
                    substring.append(r)
                longstr[s[l]] = longstr.get(s[l], 0) - 1
                l += 1
                correct -= 1
            
            else:
                break

        if (substring[-1]-substring[-0]) == 1001:
            return ""
        return s[(substring[-2]):(substring[-1] + 1)]