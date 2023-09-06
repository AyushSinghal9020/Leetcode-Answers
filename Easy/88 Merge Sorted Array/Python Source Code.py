class Solution:
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       
        nums1 = nums1[:len(nums2)]

        for val in nums2:
            
            counter = 0
            
            for index in range(len(nums1)):
                
                if val < nums1[index]: 
                    
                    nums1.insert(val , index)
                    counter += 1
                    
                    break
            
            if counter == 0:nums1.append(val)
