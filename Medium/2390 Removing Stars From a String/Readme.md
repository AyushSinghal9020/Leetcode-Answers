<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44024094-9e7003644662908aa91622ff54522f17.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231104T061709Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=a269e5a5f6f9002c424b5247053d53c1f4b1258852330e3d289f130741237fb4' width = 400><img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44024097-985b0399b5b633f5ed2484e9ff9e1f13.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231104T061733Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=25c941bde515235c1ee4e1e8c8fd438639f9f41512ec62303feed5d8d19a063b' width = 400>

# Question 2390
****
## Removing Stars From a String

****
### Problem Statement -

You are given a string `s`, which contains stars `*`.

In one operation, you can:

* Choose a star in `s`.
* Remove the closest **non-star** character to its **left**, as well as remove the star itself.
*Return the string after* **all** *stars have been removed*.

**Note:**

* The input will be generated such that the operation is always possible.
* It can be shown that the resulting string will always be unique.

### Examples
```
Input: s = "leet**cod*e"

Output: "lecoe"

Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
```
```
Input: s = "erase*****"

Output: ""

Explanation: The entire string is removed, so we return an empty string.
```
****
### Constraints
```
1 <= s.length <= 105

s consists of lowercase English letters and stars *.

The operation above can be performed on s.
```
