class Solution:
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True

            seen.add(n)
        
        return False
    

'''
Add each element to a set while iterating through the list. 
If an element is already in the set, return True (duplicate found).
'''