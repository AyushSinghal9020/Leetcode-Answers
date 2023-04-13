nums = [3,6,9,1]
nums.sort()
sum = 0
for i in range(len(nums) - 1):
    if abs(nums[i] - nums[i + 1]) > sum :
        sum = abs(nums[i] - nums[i + 1])
