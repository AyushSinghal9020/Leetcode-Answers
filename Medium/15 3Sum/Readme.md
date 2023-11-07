||||
|---|---|---|
|Python|
|Owner|<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44083946-16a2bfe2e73747f427dbdc168e9010c3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231107%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231107T132851Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=b79be095bcf6dfdce9c8e908fa40fa3f5e073a3cd0e9a9c0ce5e6dd336deebc6' width = 400>|<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44083956-a30b960cedaee744d617049e64a96afc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231107%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231107T132915Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=981671e41b0b858ba25695cec1f1b898c95d3e2656111ff58d1ab19ceb72aa25' width = 400>


# Question 15
****
## 3Sum  

****
### Problem Statement -

Given an integer array nums, return all the triplets` [nums[i], nums[j], nums[k]]` such that `i != j` , `i != k` , and `j != k`, and `nums[i] + nums[j] + nums[k]` == 0.

Notice that the solution set must not contain duplicate triplets.
### Examples
```
Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```
```
Input: nums = [0,1,1]

Output: []

Explanation: The only possible triplet does not sum up to 0.
```
```
Input: nums = [0,0,0]

Output: [[0,0,0]]

Explanation: The only possible triplet sums up to 0.
```
****
### Constraints
```
3 <= nums.length <= 3000

-10^5 <= nums[i] <= 10^5
```
