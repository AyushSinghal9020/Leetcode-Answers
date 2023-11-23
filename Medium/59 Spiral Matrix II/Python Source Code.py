class Solution:
    
    def generateMatrix(self, n: int) -> List[List[int]]:

        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        count = 1

        matrix = [[0 for _ in range(n)] for _ in range(n)]

        while count <= n ** 2 : 

            for index in range(left , right + 1) : 

                matrix[top][index] = count 
                count += 1
            top += 1

            for index in range(top , bottom + 1):

                matrix[index][right] = count
                count += 1

            right -= 1

            for index in range(right , left -1 , -1) : 

                matrix[bottom][index] = count 
                count += 1
            bottom -= 1
            
            for index in range(bottom , top -1 , -1):

                matrix[index][left] = count 
                count += 1

            left += 1

        return matrix
        
        
