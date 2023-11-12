class Solution(object):
    
    def isValidSudoku(self, board):
        
        res = []
        
        for row in range(9):
            
            for col in range(9):
                
                element = board[row][col]
                
                if element != '.' : res += [
                    (row , element) , 
                    (element , col) , 
                    (
                        row // 3 , 
                        col // 3 , 
                        element
                    )
                ]
        
        return len(res) == len(set(res))
