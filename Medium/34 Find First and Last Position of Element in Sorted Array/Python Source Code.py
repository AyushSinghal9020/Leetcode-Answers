class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        first_index = -1
        last_index = -1

        if target in nums : 

            first_index = nums.index(target)
            
            nums.reverse()
            
            last_index = nums.index(target)
            last_index = len(nums) - last_index -1

        return [first_index , last_index]
        
        
