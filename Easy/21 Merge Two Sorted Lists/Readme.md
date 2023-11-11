||||
|---|---|---|
|Python|
||<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44184788-a44696d61023e4f42c8beb94320cc2b9.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231111%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231111T095252Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=f23ede80eec06fc3134b4eba8b3bdc148f0793b7cdf6df1cf0476687aa660120' width = 400>|<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44184793-fbc5384b6de2efe356ac884f10de516f.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231111%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231111T095323Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=49cf176af329f5e28e29dbb22cc445092507319e23620f254be827a161a629e7' width = 400>


# Question 21
****
## Merge Two Sorted Lists    

****
### Problem Statement -

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

*Return the head of the merged linked list*.

### Examples
<img src = 'https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg' width = 400>

```
Input: list1 = [1,2,4], list2 = [1,3,4]

Output: [1,1,2,3,4,4]
```
```
Input: list1 = [], list2 = []

Output: []
```
```
Input: list1 = [], list2 = [0]

Output: [0]
```
****
### Constraints
```
The number of nodes in both lists is in the range [0, 50].

-100 <= Node.val <= 100

Both list1 and list2 are sorted in non-decreasing order.
```
