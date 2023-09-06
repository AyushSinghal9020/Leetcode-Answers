class Solution:
  
    def removeDuplicates(self, nums: List[int]) -> int:

        table = {}
        db = []

        for val in nums:
            
            if val in table.keys():
                
                table[val] += 1
                
                if table[val] < 1:db.append(val)
            
            else : table[val] = 0
            
