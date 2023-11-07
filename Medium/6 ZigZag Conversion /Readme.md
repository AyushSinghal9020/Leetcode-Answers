||||
|---|---|---|
|Python|
|Owner|<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44078317-39adfa8a49fd50c47692940e68b48e3f.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231107%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231107T094511Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=35b88890d4020b008769f3a1807da62c61c69e15ac6a5b642cf99b6025e8527e' width = 400>|<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44078304-1c56c42ffc804137fb46b318a0666417.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231107%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231107T094446Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=fe9c787c5f387ab1598054ecab0dc94071758c22db187cd95d238845d39023d5' width = 400>


# Question 6
****
## ZigZag Conversion  

****
### Problem Statement -

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:
```
string convert(string s, int numRows);
```
### Examples
```
Input: s = "PAYPALISHIRING", numRows = 3

Output: "PAHNAPLSIIGYIR"
```
```
Input: s = "PAYPALISHIRING", numRows = 4

Output: "PINALSIGYAHRPI"

Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
```
```
Input: s = "A", numRows = 1

Output: "A"
```
****
### Constraints
```
1 <= s.length <= 1000

s consists of English letters (lower-case 
and upper-case), ',' and '.'.

1 <= numRows <= 1000
```
