<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44051815-a064af92fc413eb4621b8c36eb178c83.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231106%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231106T105728Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=11f5ac0dd78fb06f626764cbd2cc58a3acd33c8fb3a65b3c4db5dd1a5c48111b' width = 400><img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44051824-57d2e57b01e3ee5992bd3f14ece6e705.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231106%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231106T105757Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=826b273efa78034e892f581faec6e40655b7c9fd2a92fca21d9a86b530327afb' width = 400>

# Question 4
****
## Meidan of Two Sorted Arrays

****
### Problem Statement -

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

### Examples
```
Input: nums1 = [1,3], nums2 = [2]

Output: 2.00000

Explanation: merged array = [1,2,3] and median is 2.
```
```
Input: nums1 = [1,2], nums2 = [3,4]

Output: 2.50000

Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```
```
Input: s = "pwwkew"

Output: 3

Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```
****
### Constraints
```
nums1.length == m

nums2.length == n

0 <= m <= 1000

0 <= n <= 1000

1 <= m + n <= 2000

-106 <= nums1[i], nums2[i] <= 106
```
