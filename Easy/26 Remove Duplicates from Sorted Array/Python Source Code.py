class Solution:
  
    def removeDuplicates(self, nums: List[int]) -> int:
      
        db = []
        
        for val in nums:
            
          if val not in db:db.append(val)
        
        nums = db + ['_'] * (len(nums) - len(db))
        
        return len(db)
