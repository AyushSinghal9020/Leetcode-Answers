<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44011865-043d6cc57625ad6ad869da36dd67dd2a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231103%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231103T135133Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=407eca1185479b1d85be2dec3ce0eefbf8b8848cbc032593859271b2d42cac78' width = 400><img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44011853-486815d0aa6467f7b7f6504f4b0a17e0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231103%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231103T135114Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=ea8e63f01a3fc7880ddb1840f17bba94be4f52f6c12e2167f655ecbe93fb83e7' width = 400>

# Question 1657
****
## Determine if Two Strings Are Close

****
### Problem Statement -

Two strings are considered **close** if you can attain one from the other using the following operations:

* Operation 1: Swap any two **existing** characters.
* For example, `abcde -> aecdb`
* Operation 2: Transform **every** occurrence of one **existing** character into another **existing** character, and do the same with the other character.
* For example, `aacabb -> bbcbaa` (all `a`'s turn into `b`'s, and all `b`'s turn into `a`'s)

You can use the operations on either string as many times as necessary.

Given two strings, `word1` and `word2`, return `true` if `word1` and `word2` are **close** , *and* `false` *otherwise*.
### Examples
```
Input: word1 = "abc", word2 = "bca"

Output: true

Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
```
```
Input: word1 = "a", word2 = "aa"

Output: false

Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
```
```
Input: word1 = "cabbba", word2 = "abbccc"

Output: true

Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
```

****
### Constraints
```
1 <= word1.length, word2.length <= 105

word1 and word2 contain only lowercase English letters.
```
