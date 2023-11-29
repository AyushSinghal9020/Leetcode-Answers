||||
|---|---|---|
|Python|
||<img src = 'https://raw.githubusercontent.com/ayush7823/sample-/main/Construct-Binary-Tree-from-Preorder-and-Inorder-Traversal-LeetCode%20(1).png' width = 400>|<img src = 'https://raw.githubusercontent.com/ayush7823/sample-/main/Construct-Binary-Tree-from-Preorder-and-Inorder-Traversal-LeetCode.png' width = 400>


# Question 105
****
## Construct Binary Tree from Preorder and Inorder Traversal 

****
### Problem Statement -

Given two integer arrays `preorder` and `inorder` where preorder is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return *the binary tree*.

### Examples
<img src = 'https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg'  width = 400>

```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]

Output: [3,9,20,null,null,15,7]
```
```
Input: preorder = [-1], inorder = [-1]

Output: [-1]
```
****
### Constraints
```
1 <= preorder.length <= 3000

inorder.length == preorder.length

-3000 <= preorder[i], inorder[i] <= 3000

preorder and inorder consist of unique values.

Each value of inorder also appears in preorder.

preorder is guaranteed to be the preorder traversal of the tree.

inorder is guaranteed to be the inorder traversal of the tree.
```
