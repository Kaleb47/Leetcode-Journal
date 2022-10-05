class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # map the character count to each string to the list of anagrams
        
        for s in strs:
            count = [0] * 26 # one for each possible character
        
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return res.values()
