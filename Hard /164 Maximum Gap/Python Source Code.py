class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        if len(nums) < 2: return sum
        else :
            for i in range(len(nums) - 1):
                if abs(nums[i] - nums[i + 1]) > sum :
                    sum = abs(nums[i] - nums[i + 1])
            return sum
