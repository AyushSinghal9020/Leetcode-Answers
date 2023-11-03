<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44010989-2322fc4f3baa0831ecf614fc9cd299fb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231103%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231103T132111Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=1e2ec79f6ea27b4bd9f7a31e6596b96c3c5847f3c0f7d99a15ecb17bc845c0a7' width = 400><img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44011001-c5941ba677c92db184c326627154ea83.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231103%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231103T132136Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=a1ac94ed5db3a7c39e9d798309d8abdf0843a04b0e21b1aa0b7a4dbb69ee76c5' width = 400>

# Question 2215
****
## Find the Difference of Two Arrays

****
### Problem Statement -

Given two **0-indexed** integer arrays `nums1` and `nums2`, *return a list* `answer` *of size* `2` *where*:

* `answer[0]` *is a list of all* **distinct** *integers in* `nums1` *which are not present in* `nums2`.
* `answer[1]` *is a list of all* **distinct** *integers in* `nums2` *which are not present in* `nums1`.

**Note** that the integers in the lists may be returned in **any** order.
### Examples
```
Input: nums1 = [1,2,3], nums2 = [2,4,6]

Output: [[1,3],[4,6]]

Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
```
```
Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]

Output: [[3],[]]

Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
```

****
### Constraints
```
1 <= nums1.length, nums2.length <= 1000

-1000 <= nums1[i], nums2[i] <= 1000
```
