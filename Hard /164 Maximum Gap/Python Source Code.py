nums = [3,6,9,1]
nums.sort()
for i in range(len(nums) - 1):
    print(abs(nums[i] - nums[i + 1]))
