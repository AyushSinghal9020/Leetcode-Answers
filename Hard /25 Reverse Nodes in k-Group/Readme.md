||||
|---|---|---|
|Python|
||<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44186184-5a91e613c0ceed027a97808ecbca8fa9.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231111%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231111T125838Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=f4beaa40fe4decf48dbcff810ae75916cec4e4c1e3082aa9edd637f80ee739ab' width = 400>|<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44186190-bfc379d692efa27e4401db5fc510b096.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231111%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231111T125850Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=bc11a4c3f76d2d67947816745e004e767868e6fa3c99d1b9c8ba1ae6457de7dc' width = 400>


# Question 25
****
## Reverse Nodes in k-Group    

****
### Problem Statement -

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the *modified list*.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

### Examples
<img src = 'https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg' width = 400>

```
Input: head = [1,2,3,4,5], k = 2

Output: [2,1,4,3,5]
```
<img src = 'https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg' width = 400>

```
Input: head = [1,2,3,4,5], k = 3

Output: [3,2,1,4,5]
```
****
### Constraints
```
The number of nodes in the list is n.

1 <= k <= n <= 5000

0 <= Node.val <= 1000
```
