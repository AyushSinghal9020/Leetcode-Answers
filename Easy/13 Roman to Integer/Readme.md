||||
|---|---|---|
|Python|
||<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44134391-8c5b3e2df203bb49365bc9d113db3963.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231109%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231109T081451Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=e8571abfa1a621f1c53edf8cce58144163843415814492498f116a95bba81bca' width = 400>|<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44134423-027a0829efa4bca908ec50debf91d04f.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231109%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231109T081610Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=470a353cb975314c80aa92e95cdd015fb8da8c68218e32b956509d4207bc3fef' width = 400>


# Question 13
****
## Roman to Integer  

****
### Problem Statement -

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, `2` is written as `II` in Roman numeral, just two one's added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

* `I` can be placed before` V` (5) and `X` (10) to make 4 and 9. 
* `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
* `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

### Examples
```
Input: s = "III"

Output: 3

Explanation: III = 3.
```
```
Input: s = "LVIII"

Output: 58

Explanation: L = 50, V= 5, III = 3.
```
```
Input: s = "MCMXCIV"

Output: 1994

Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```
****
### Constraints
```
1 <= s.length <= 15

s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').

It is guaranteed that s is a valid roman numeral in the range [1, 3999].

```
