nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
nums1 = nums1[:len(nums2)] 
 
for i in nums2:
    for j in range(len(nums1)):
        if i < nums1[j]:
            nums1.insert(j , i)
nums1
