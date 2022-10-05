import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # sanitize
        
        regex = re.compile('[^a-zA-Z0-9]')
        s = regex.sub('', s)
        
        s = s.lower()
        s = s.replace(" ", "")
        if (len(s) <= 1):
            return True
        
        if (len(s) < 3):
            return s[0] == s[1]
        
        set1 = s[: int( (len(s) / 2))]
        if ( (len(s) % 2) == 0):
            set2 = s[int( (len(s) / 2) ) :]
        else:
            set2 = s[int( (len(s) / 2) + 1) :]
            
        return set1 == set2[::-1]
                
        
        # how to find the middle of a string?
        # only strings that are odd length have a middle indexed
        # how to find the middle of an even length string?
        # amana plana c analp anama
        # 21 characters long, the 10 character, 0-9 is amana plana, 11-21 analp anama
        # the first set of letters is equal to reverse of the second set
        # if its even: redder 0-2 3-5, set 1 and set 2
        # 1st set = 0 to (length / 2) -1 
        # 2 set = (length / 2) + 1 to (length - 1)
        ## EVEN PALINDROME
        # set1 == set2[::-1]
        # set2 = a[ int((len(a) / 2)) :]
        # set1 = a[: int((len(a) / 2))]
        
        ## ODD PALINDROME
        #  set1 = x[: int((len(x) / 2))]
        # set2 = x[int((len(x) / 2) + 1):]
        # set1 == set2[::-1]
        
        # this is because int rounds the number down, flooring the integer
        # (len(x) % 2) == 0 this is how we check if it even or odd
        
        # uncapitalize remove x.lower()
        #remove whitespace string.replace(" ", "")r
        # remove non-letter characters
        #import re

        #regex = re.compile('[^a-zA-Z]')
        #First parameter is the replacement, second parameter is your input string
        #regex.sub('', 'ab3d*E')
        #Out: 'abdE'
        
        # a[0] == a[-1]
