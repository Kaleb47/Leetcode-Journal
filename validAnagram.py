
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = map()
        
        for s and t in self:
            if s and t in hashmap:
                return True
            hashmap.add(s, t)
        return False
