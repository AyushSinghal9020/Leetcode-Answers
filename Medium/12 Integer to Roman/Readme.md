||||
|---|---|---|
|Python|
||<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44133862-9a66ccc3c95813fdfe8b36026635b523.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231109%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231109T075114Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=4f603636f3756db045bf674f0e8196262eda51ace51cd9cae4b7ded5b3d77fd1' width = 400>|<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44133879-4fd7155cf1e30e6a1613c7a1ba0dd28e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231109%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231109T075148Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=572c67ffa4fac8bec7b0fe744087022eccbefa57f34983b4989943589398e8a9' width = 400>


# Question 12
****
## Integer to Roman  

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

Given an integer, convert it to a roman numeral.

### Examples
```
Input: num = 3

Output: "III"

Explanation: 3 is represented as 3 ones.
```
```
Input: num = 58

Output: "LVIII"

Explanation: L = 50, V = 5, III = 3.
```
```
Input: num = 1994

Output: "MCMXCIV"

Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```
****
### Constraints
```
1 <= num <= 3999
```
