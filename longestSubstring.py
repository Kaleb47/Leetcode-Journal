class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #longest substring without repeating characters
        #that means we need the len() method to count up until a repeating character
        
        # there should be a loop that finds the length of the substring but breaks until the character repeats
        
        # while loop through the string until a repeating character is found
        
         # constraints
          # no repeating characters  
        
        charSet = set()
        
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
