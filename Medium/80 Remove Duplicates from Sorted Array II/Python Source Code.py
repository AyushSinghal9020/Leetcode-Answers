class Solution:
    
    def removeDuplicates(self, nums: list[int]) -> int:
        
        og = []
        
        for i in nums:
            
            if i not in og:
                
                og.append(i)

        return len(og)
