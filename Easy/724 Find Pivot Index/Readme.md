<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44010651-6210840c94a6135f1f897c7f2c9aa3ed.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231103%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231103T130853Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=280d6d68ad4fca515584018941fbc76a2f28cec52c3ff4e9514b16f06d05fa09' width = 400><img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44010664-fb3d5ec29af25e80034e5d906eb5e051.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231103%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231103T130927Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=22da422d95c59703202103c005ca4d0e7e8a410b8cdff121f86ea1d69c8b191c' width = 400>

# Question 724
****
## Find Pivot Index

****
### Problem Statement -

Given an array of integers `nums`, calculate the **pivot index** of this array.

The **pivot index** is the index where the sum of all the numbers **strictly** to the left of the index is equal to the sum of all the numbers **strictly** to the index's right.

If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.

Return the **leftmost pivot index**. If no such index exists, return `-1`.
### Examples
```
Input: nums = [1,7,3,6,5,6]

Output: 3

Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
```
```
Input: nums = [1,2,3]

Output: -1

Explanation:
There is no index that satisfies the conditions in the problem statement.
```
```
Input: nums = [2,1,-1]

Output: 0

Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
```

****
### Constraints
```
1 <= nums.length <= 104

-1000 <= nums[i] <= 1000
```

Note: This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/
