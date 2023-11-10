class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:

        look_up = []

        for index in range(len(nums)):

            if nums[index] in look_up : nums[index] = 101
            else : look_up.append(nums[index])

        nums.sort()

        for index in range(-1 , -len(nums) , -1):
            
            if nums[index] == 101 : nums[index] = '_' 
            else : break

        return len(look_up)
