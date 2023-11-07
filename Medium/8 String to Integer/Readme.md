||||
|---|---|---|
|Python|
||<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44079470-8ca961704ea8894d5ac8a9911b3232e0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231107%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231107T103334Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=51e9cc1a2279538bef2e7ac5ae2ceac46a5d7e100dc3f978f7d6886dc2400fee' width = 400>|<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44079479-9f4c93199db754611c28ca8cbe95b8d6.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231107%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231107T103351Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=4d923136cbe383aefe7f920e176bab8c4d8414462b7186c62d7742423fc32f25' width = 400>


# Question 8
****
## String to Integer (atoi)  

****
### Problem Statement -

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to C/C++'s `atoi` function).

The algorithm for `myAtoi(string s)` is as follows:

* Read in and ignore any leading whitespace.
* Check if the next character (if not already at the end of the string) is `'-'` or `'+'`. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
* Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
* Convert these digits into an integer (i.e. `"123" -> 123`, `"0032" -> 32`). If no digits were read, then the integer is `0`. Change the sign as necessary (from step 2).
* If the integer is out of the 32-bit signed integer range `[-2^31, 2^31 - 1]`, then clamp the integer so that it remains in the range. Specifically, integers less than `-2^31` should be clamped to `-2^31`, and integers greater than `2^31 - 1` should be clamped to `2^31 - 1`.
* Return the integer as the final result.

**Note:**

* Only the space character `' '` is considered a whitespace character.
* **Do not ignore** any characters other than the leading whitespace or the rest of the string after the digits.

### Examples
```
Input: s = "42"

Output: 42

Explanation: The underlined characters 
are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
```
```
Input: s = "   -42"

Output: -42

Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
```
```
Input: s = "4193 with words"

Output: 4193

Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
```
****
### Constraints
```
0 <= s.length <= 200

s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
```
