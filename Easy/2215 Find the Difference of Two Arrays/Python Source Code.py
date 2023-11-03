class Solution:
    
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        answer_0 = [
            val 
            for val 
            in nums1 
            if val not in nums2
        ]        
        answer_1 = [
            val 
            for val 
            in nums2
            if val not in nums1
        ]

        out = [list(set(answer_0)) , list(set(answer_1))]

        return out
