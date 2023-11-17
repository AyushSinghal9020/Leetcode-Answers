class Solution:
  
  def jump(self, nums: List[int]) -> int:
    
    ans = 0
    end = 0
    farthest = 0

    for index in range(len(nums) - 1):
      
      farthest = max(farthest, index + nums[index])
      
      if farthest >= len(nums) - 1:
        
        ans += 1
        break
      
      if index == end:      
        
        ans += 1        
        end = farthest  

    return ans
