class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # swap k characters with an english uppercase letter day
        # return the length of the that substring
        # possible methods to replace one character with another
        
        
        
        # we need a for loop to find the length of the largest string
        # then we nee a while loop the replace the characters x number of times
        
        # calculate the length of characters via windowlen - Count[B]
        
        # take our window, start at the beginning and exapnd as much as we can until the string is valid
        # if not valid, shift to the left and start again
        #so we define a left and right pointer
        
        
        
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
          count[s[r]] = 1 + count.get(s[r], 0)
          maxf = max(maxf, count[s[r]])

          if (r -l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1

          res = max(res, r - l + 1)
        return res
