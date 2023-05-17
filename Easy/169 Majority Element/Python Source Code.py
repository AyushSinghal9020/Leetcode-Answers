class Solution:
    
    def majorityElement(self, nums: list[int]) -> int:
        
        uni = {}

        for i in nums:
            
            if i in uni.keys():
                
                uni[i] += 1
            
            else :
                
                uni[i] = 1

        return [i for i in uni if uni[i]==max(uni.values())][0]
