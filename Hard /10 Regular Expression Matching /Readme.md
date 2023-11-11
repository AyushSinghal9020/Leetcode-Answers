||||
|---|---|---|
|Python|
||<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44184059-48405868dad4e49a48565398412ec9dc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231111%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231111T075530Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=485898c8eb4a7b218d75e7c8f487ebba50e61b0b8181892c8d3e1252f8a6dd1e' width = 400>|<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44184065-8d3d9ac44bd5fe61aaee1406a9e119ad.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231111%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231111T075605Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=7ec57b4e383a01180fa5bd00b0e300e1c917e0775b1c79fff3587bc98b3e9a1e' width = 400>


# Question 10
****
## Regular Experssion Matching    

****
### Problem Statement -

Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:

* `'.'` Matches any single character.​​​​
* `'*'` Matches zero or more of the preceding element.

The matching should cover the **entire** input string (not partial).

### Examples

```
Input: s = "aa", p = "a"

Output: false

Explanation: "a" does not match the entire string "aa".
```
```
Input: s = "aa", p = "a*"

Output: true

Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```
```
Input: s = "ab", p = ".*"

Output: true

Explanation: ".*" means "zero or more (*) of any character (.)".
```
****
### Constraints
```
1 <= s.length <= 20

1 <= p.length <= 20

s contains only lowercase English letters.

p contains only lowercase English letters, '.', and '*'.

It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
```
