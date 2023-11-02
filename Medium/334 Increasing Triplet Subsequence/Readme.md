<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/43985280-d45b4be3169fbb500b049ef9c5a13749.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231102%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231102T130713Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=5ee5053da4cbb8a2909e94cf089c583daeef3c57c443907ab58048d9efc28f3a' width = 400><img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/43985289-b5670ac2e4be4862ee4826af9e645dd1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231102%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231102T130733Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=803da198fd5ed6650fe5f0e6d150d91c1d6edba300c92dba3cf183d72d82b552' width = 400>

# Question 334
****
## Increasing Triplet Subsequence

****
### Problem Statement -

Given an integer array `nums`, return `true` *if there exists a triple of indices* `(i, j, k)` *such that* `i < j < k` *and* `nums[i] < nums[j] < nums[k]`. If no such indices exists, return `false`
### Examples
```
Input: nums = [1,2,3,4,5]

Output: true

Explanation: Any triplet where i < j < k is valid.
```
```
Input: nums = [2,1,5,0,4,6]

Output: true

Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
```

****
### Constraints
```
1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
```

**Follow up**: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?


