class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1 = nums1[:len(nums2)]
        for i in nums2:
            for j in range(len(nums1)):
                if i < nums1[j]:
                    nums1.insert(j , i)
                    nums2.pop(0)
                    break
        nums1 = nums1 + nums2
        return nums1
