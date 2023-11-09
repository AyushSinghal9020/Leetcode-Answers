class Solution:
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums_length = len(nums)
        nums.sort()
        
        max_diff = 20001
        min_diff = 0
        
        for index in range(nums_length):
            
            right_index = index + 1
            end_index = nums_length - 1
            
            while(right_index<end_index):
                
                window_sum = nums[index] + nums[right_index] + nums[end_index]
                target_diff = abs(window_sum - target)
                
                if(target_diff < max_diff):
                    
                    max_diff = target_diff
                    min_diff = window_sum
                
                if(window_sum == target) : return target
                elif(window_sum < target) : right_index += 1
                else : end_index -= 1
            
        return min_diff
