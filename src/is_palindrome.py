class Solution:
    def isPalindrome(self, s: str) -> bool:
        validS = (''.join(c for c in s if c.isalnum())).lower()
        l = 0
        r = len(validS) - 1
        while (l < r):
            if validS[l] != validS[r]:
                return False
            
            l += 1
            r -= 1
        
        return True