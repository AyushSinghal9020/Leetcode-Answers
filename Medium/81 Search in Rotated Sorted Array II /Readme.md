||||
|---|---|---|
|Python|
||<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44171036-5843cab4fea3f196a03f795f547cf31f.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231110%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231110T133934Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=79116055c0344dfc3942fabfa50d3b01ecc817a4a68045c59589839f79943bb7' width = 400>|<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44171053-eca71c3ed93553aa56e6919a969e099c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231110%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231110T134014Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=4932ebf769d4381f5fdabf80d19cb1584ce0e8b48f1039b21d362ea5cf12fdd7' width = 400>


# Question 81
****
## Search in Rotated Sorted Array II  

****
### Problem Statement -

There is an integer array `nums` sorted in non-decreasing order (not necessarily with **distinct** values).

Before being passed to your function, `nums` is **rotated** at an unknown pivot index `k` (`0 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` **(0-indexed)**. For example, `[0,1,2,4,4,4,5,6,6,7]` might be rotated at pivot index `5` and become `[4,5,6,6,7,0,1,2,4,4]`.

Given the array `nums` **after** the rotation and an integer `target`, return `true` *if* `target` *is in* `nums`, *or* `false` *if it is not in* `nums`.

You must decrease the overall operation steps as much as possible.

### Examples
```
Input: nums = [2,5,6,0,0,1,2], target = 0

Output: true
```
```
Input: nums = [2,5,6,0,0,1,2], target = 3

Output: false
```
****
### Constraints
```
1 <= nums.length <= 5000

-104 <= nums[i] <= 104

nums is guaranteed to be rotated at some pivot.

-104 <= target <= 104
```

**Follow up:** This problem is similar to Search in Rotated Sorted Array, but `nums` may contain **duplicates**. Would this affect the runtime complexity? How and why?
