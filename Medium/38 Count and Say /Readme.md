||||
|---|---|---|
|Python|
||<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44194535-9cfdbbc29cdf4baa7bf6879a6240cd3a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231112%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231112T094918Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=a6d6ec2f2c85bed114bded9f1711645ed85ef65d91cd5d2d2d850eae8b95e7a0' width = 400>|<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44194539-d0eedfec6732b9dcf8f25ec6ca50007b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231112%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231112T094937Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=87500e544f2a31dd652a77b10822c8143918f8f589f5124e3801380c8b9edd36' width = 400>


# Question 38
****
## Count and Say 

****
### Problem Statement -

The **count-and-say** sequence is a sequence of digit strings defined by the recursive formula:

* `countAndSay(1) = "1"`
* `countAndSay(n)` is the way you would "say" the digit string from `countAndSay(n-1)`, which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the **minimal** number of substrings such that each substring contains exactly **one** unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":

<img src = 'https://assets.leetcode.com/uploads/2020/10/23/countandsay.jpg' wdith = 400>
Given a positive integer `n`, return the `nth` term of the **count-and-say** sequence.

### Examples

```
Input: n = 1

Output: "1"

Explanation: This is the base case.
```
```
Input: n = 4

Output: "1211"

Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
```
****
### Constraints
```
1 <= n <= 30
```
