# <----------METHOD 1---------->

class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)

        def bs(value , recur_nums):
            
            if len(recur_nums) == 1 : 
                if recur_nums[0] + value == 0: return recur_nums
                else : return None

            if len(recur_nums) == 2:
                if recur_nums[0] + value == 0 : return [recur_nums[0]]
                if recur_nums[1] + value == 0 : return [recur_nums[1]]

            middle = recur_nums[len(recur_nums) // 2]

            if middle >= - value : return bs(value , 
            list(recur_nums[: len(recur_nums) // 2]))
            return bs(value , 
                        list((recur_nums[len(recur_nums) // 2 :])))

        outs = []

        for index in range(len(nums) - 2) : 

            window = nums[index  : index + 2]
            triplet = bs(sum(window) , list(nums[index + 2 :]))

            if triplet : outs.append(window + list(triplet))

        if outs == []: return outs        
        return list(set(outs)) 

# <----------METHOD 2---------->

class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        target = 0
        nums.sort()
        s = set()
        output = []
        
        for i in range(len(nums)):
            
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                
                sum = nums[i] + nums[j] + nums[k]
                
                if sum == target:
                    
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                
                elif sum < target:j += 1
                else:k -= 1
        
        output = list(s)
        
        return output
