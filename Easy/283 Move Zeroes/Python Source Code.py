class Solution:
    
    def moveZeroes(self, nums: List[int]) -> None:
        
        """
        Do not return anything, modify nums in-place instead.
        """
        
        leng = len(nums)
        
        for index in range(-1 , -leng -1 , -1):

            if nums[index] == 0:

                nums.pop(index)
                nums.append(0)
