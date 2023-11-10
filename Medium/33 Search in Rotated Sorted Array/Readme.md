||||
|---|---|---|
|Python|
||<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44171532-d6867f5447de01f9aa42434d70c63ee2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231110%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231110T140336Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=792406babfd84324e9e2323a43a44a924097d961c8c80059fd4013b6b88dd819' width = 400>|<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44171537-1a4e65caac755f2838b35cfb51afd544.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231110%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231110T140350Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=a709176ac6c8bcbae8525a1e89de6b5159e401ecebcf4bb3c3cbff789c458e7c' width = 400>


# Question 33
****
## Search in Rotated Sorted Array   

****
### Problem Statement -

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return *the index of* `target` *if it is in* `nums`, *or* `-1` *if it is not in* `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

### Examples
```
Input: nums = [4,5,6,7,0,1,2], target = 0

Output: 4
```
```
Input: nums = [4,5,6,7,0,1,2], target = 3

Output: -1
```
```
Input: nums = [1], target = 0

Output: -1
```
****
### Constraints
```
1 <= nums.length <= 5000

-104 <= nums[i] <= 104

All values of nums are unique.

nums is an ascending array that is possibly rotated.

-104 <= target <= 104
```
