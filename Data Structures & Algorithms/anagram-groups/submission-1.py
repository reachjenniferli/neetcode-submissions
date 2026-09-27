class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #initialize dictionary
        anagram_map = defaultdict(list)
        #iterate through list
        for word in strs:
            #sort word
            sorted_word = ''.join(sorted(word))
            #add sorted word to map
            anagram_map[sorted_word].append(word)
        #return list
        return anagram_map.values()
