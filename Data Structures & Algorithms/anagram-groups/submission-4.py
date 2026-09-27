class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = list()
        anagrams = list()


        for n in strs:
            anagram = sorted(n)
            if anagram not in anagrams:
                anagrams.append(anagram)
                res.append([n])
            else:
                for i, a in enumerate(anagrams):
                    if a == anagram:
                        res[i].append(n)

        return res