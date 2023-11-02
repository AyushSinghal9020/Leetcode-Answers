<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/43989206-591d7c5644b406af5c374ec8c6c1e054.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231102%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231102T154027Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=a3a34e62c353246d5630ed57b96ebe620de79790bccbcec13c9c337cb55cfdfd' width = 400><img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/43989216-1790eba725456c5b920cce9b6ee0bb8e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231102%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231102T154044Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=f25fb1ea1706a0048535eaa100a1dbbc762a2be48c8c3f2a1a6e7473c985cb69' width = 400>

# Question 392
****
## Is Subsequence

****
### Problem Statement -

Given two strings `s` and `t`, return `true` if `s` is a **subsequence** of `t`, or `false` *otherwise*.

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).
### Examples
```
Input: s = "abc", t = "ahbgdc"

Output: true
```
```
Input: s = "axc", t = "ahbgdc"

Output: false
```

****
### Constraints
```
0 <= s.length <= 100

0 <= t.length <= 104

s and t consist only of lowercase English letters
```

**Follow up**: Suppose there are lots of incoming `s`, say `s1, s2, ..., sk` where `k >= 10^9`, and you want to check one by one to see if `t` has its subsequence. In this scenario, how would you change your code?
