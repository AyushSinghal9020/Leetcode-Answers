||||
|---|---|---|
|Python|
||<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4940162/44310379-e2caf2cbb78e424fd6370a6c32d46356.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231117T030405Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=8800089632569e99ed76d75d3f6148396197cffcf0ed383470ba20d7510b41d8' width = 400>|<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4940162/44310385-64433a876f74b59b0a4e069cf3afa396.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231117%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231117T030425Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=2b8391da58a360ac02333055eaebaabee324834dbb795964f5cace604612ffa4' width = 400>


# Question 45
****
## Jump Game II

****
### Problem Statement -

You are given a **0-indexed** array of integers `nums` of length `n`. You are initially positioned at `nums[0]`.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at `nums[i]`, you can jump to any `nums[i + j]` where:

* `0 <= j <= nums[i]` and
* `i + j < n`
Return *the minimum number of jumps to reach* `nums[n - 1]`. The test cases are generated such that you can reach `nums[n - 1]`.

### Examples


```
Input: nums = [2,3,1,1,4]

Output: 2

Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
```
```
Input: nums = [2,3,0,1,4]

Output: 2
```
****
### Constraints
```
1 <= nums.length <= 104

0 <= nums[i] <= 1000

It's guaranteed that you can reach nums[n - 1].
```
