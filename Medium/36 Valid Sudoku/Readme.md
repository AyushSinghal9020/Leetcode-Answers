||||
|---|---|---|
|Python|
||<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44194329-aab29a9d6e10aa5130907478479d3eb3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231112%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231112T092247Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=dbf4ccf1baf880dcd459343cffae98ed4c4f80e403336b591cc8ea3c3b20e7cb' width = 400>|<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44194332-143e3d7871121c099c04f6829ca7f260.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231112%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231112T092306Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=d5f329c4a62e6057cbe6f0649b70f83afafebe69e06507a41728666d2c12e7c9' width = 400>


# Question 36
****
## Valid Sudoku

****
### Problem Statement -

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated **according to the following rules:**

* Each row must contain the digits `1-9` without repetition.
* Each column must contain the digits `1-9` without repetition.
* Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

**Note:**

* A Sudoku board (partially filled) could be valid but is not necessarily solvable.
* Only the filled cells need to be validated according to the mentioned rules.

### Examples
<img src = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png' width = 400>

```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Output: true
```
```
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Output: false

Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```
```
Input: s = ""
Output: 0
```
****
### Constraints
```
board.length == 9

board[i].length == 9

board[i][j] is a digit 1-9 or '.'.
```
