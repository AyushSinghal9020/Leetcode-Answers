# <-------------METHOD 1------------->

class Solution:
    
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        maxi = 
        leng = len(nums)

        for index in range(0 , leng - k + 1):

            average = sum(nums[index : index + k]) / k

            if average > maxi: maxi = average

        if leng == k : return sum(nums) / k

        return maxi

# <-------------METHOD 2------------->

class Solution:
   
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        currSum = maxSum = sum(nums[:k])

        for i in range(k, len(nums)):

            currSum += nums[i] - nums[i - k]
            
            maxSum = max(maxSum, currSum)

        return maxSum / k

        
