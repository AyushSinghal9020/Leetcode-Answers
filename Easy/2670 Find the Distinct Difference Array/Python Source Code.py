class Solution:
    
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        
        out = [
            len(set(nums[: i + 1])) - len(set(nums[i + 1 : ]))
            for i in range(len(nums))
            ]
        
        return out
