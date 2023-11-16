||||
|---|---|---|
|Python|
||<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4940162/44298116-f909c5c0e38defdb8188150bb896fc26.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231116%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231116T152306Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=98bfcf0d87112accb7b93547e4570de7cc6804d1d44ec24b768a18db5de06a03' width = 400>|<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4940162/44298112-d24c89b971037150db3142e331ab2630.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231116%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231116T152249Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=9dc429ab0c8b97fe69a6123b60b83ba565ce79189c80a884834898704a1d5c4e' width = 400>


# Question 42
****
## Trapping Rain Water

****
### Problem Statement -

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

### Examples
<img src = 'https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png'>

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]

Output: 6

Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```
```
Input: height = [4,2,0,3,2,5]

Output: 9
```
****
### Constraints
```
n == height.length

1 <= n <= 2 * 10^4

0 <= height[i] <= 10^5
```
