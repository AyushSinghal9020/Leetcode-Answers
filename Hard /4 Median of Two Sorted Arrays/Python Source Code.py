class Solution:
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums = nums1 + nums2
        nums = sorted(nums)

        if len(nums) % 2 == 0 :
            median = (nums[len(nums) // 2] + nums[(len(nums) // 2) - 1]) / 2
            print(len(nums) // 2)
        else : median = nums[len(nums) // 2]

        return median
