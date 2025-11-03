class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        freqMap = {}

        for letter in s:
            if letter in freqMap:
                freqMap[letter] += 1
            else:
                freqMap[letter] = 1
        
        for letter in t:
            if letter in freqMap:
                freqMap[letter] -= 1
            else:
                return False

        
        for f in freqMap:
            if freqMap[f] != 0:
                return False
        
        return True
    