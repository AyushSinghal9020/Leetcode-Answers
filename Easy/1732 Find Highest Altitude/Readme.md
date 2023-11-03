<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44009337-1f4242db47a11d2ba60af7a80c22f7b7.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231103%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231103T121321Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=622ee4964c4c120010ee809afc099a53e288a131761e04ead0975559564e0357' width = 400><img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44009326-f4391435f2536b5cfd0c5398dc75d22f.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231103%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231103T121249Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=672c8c43077e962472a89d34865a2fa56ad973fca0fbfb83cbb0d0d4fb73ec01' width = 400>

# Question 1732
****
## Maximum Average Subarray I

****
### Problem Statement -

There is a biker going on a road trip. The road trip consists of `n + 1` points at different altitudes. The biker starts his trip on point `0` with altitude equal `0`.

You are given an integer array `gain` of length `n` where `gain[i]` is the **net gain in altitude** between points `i`​​​​​​ and `i + 1` for all `(0 <= i < n)`. Return the **highest altitude** of a point.
### Examples
```
Input: gain = [-5,1,5,0,-7]

Output: 1

Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
```
```
Input: gain = [-4,-3,-2,-1,4,3,2]

Output: 0

Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0
```

****
### Constraints
```
n == gain.length

1 <= n <= 100

-100 <= gain[i] <= 100
```
