<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44026190-f64048038a308a69fee9e441a461e468.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231104T110830Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=a846fd9a888c9fc0c2e152bc50f229fc313495aa29df99c02dc986f8bf3bff9c' width = 400><img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44026197-7c6ad66e74e90415e064f831094568ff.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231104T110940Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=56fd3edbcacee38f7a30ab8209bfa68a538bc64f5a494ea7a16ced9019f53efa' width = 400>

# Question 2095
****
## Delete the Middle Node of a Linked List

****
### Problem Statement -

You are given the `head` of a linked list. **Delete** the **middle node**, and return *the* `head` *of the modified linked list*.

The **middle node** of a linked list of size `n` is the `⌊n / 2⌋th` node from the **start** using **0-based indexing**, where `⌊x⌋` denotes the largest integer less than or equal to `x`.

* For `n` = `1`, `2`, `3`, `4`, and `5`, the middle nodes are `0`, `1`, `1`, `2`, and `2`, respectively.

### Examples
```
Input: head = [1,3,4,7,1,2,6]

Output: [1,3,4,1,2,6]

Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node.
```
```
Input: head = [1,2,3,4]

Output: [1,2,4]

Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
```
```
Input: head = [2,1]

Output: [2]

Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
```
****
### Constraints
```
The number of nodes in the list is in the range [1, 105].

1 <= Node.val <= 105
```
