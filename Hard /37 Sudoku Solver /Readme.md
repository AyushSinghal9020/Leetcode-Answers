||||
|---|---|---|
|Python|
||<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44194412-dbe4ce0b0f2a00f489ad8c82669920d3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231112%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231112T093545Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=4a789ca049fdb3ec1e65584bc904e00d975ac6c27071c3787dcf19707f4e61df' width = 400>|<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44194419-6cc2b5fc7e06a0f0c4104713b7c37b0b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231112%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231112T093619Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=2997363d0c10252086552d45f61ad1339f6ef68eecccdd230d66c4d85cff5597' width = 400>


# Question 37
****
## Sudoku Solver 

****
### Problem Statement -

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy **all of the following rules:**

* Each of the digits `1-9` must occur exactly once in each row.
* Each of the digits `1-9` must occur exactly once in each column.
* Each of the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.

The `'.'` character indicates empty cells.

### Examples
<img src = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png' width = 400>

```
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:
```
<img src = 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png' width = 400>

****
### Constraints
```
board.length == 9

board[i].length == 9

board[i][j] is a digit or '.'.

It is guaranteed that the input board has only one solution.
```
