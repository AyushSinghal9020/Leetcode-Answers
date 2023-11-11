||||
|---|---|---|
|Python|
||<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44184877-e4cd314864d9ae3b8fc2eae8019a22df.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231111%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231111T100331Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=61698911f82e6dda9cee531f280787b40408bb10819465637bf27853e6d456e3' width = 400>|<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44184890-2b5c67bbdf3dea90735af04e73378324.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231111%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231111T100426Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=3b9645cd1efc23384c9ae92cdbfa51196c420e51f6c6bda1b082ff8e3e9ce82b' width = 400>


# Question 23
****
## Merge k Sorted Lists    

****
### Problem Statement -

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it*.

### Examples
<img src = 'https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg' width = 400>

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]

Output: [1,1,2,3,4,4,5,6]

Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```
```
Input: lists = []

Output: []
```
```
Input: lists = [[]]

Output: []
```
****
### Constraints
```
k == lists.length

0 <= k <= 104

0 <= lists[i].length <= 500

-104 <= lists[i][j] <= 104

lists[i] is sorted in ascending order.

The sum of lists[i].length will not exceed 104.
```
