class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix : return []

        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        result = []

        while len(result) < rows * cols : 

            result += [
                matrix[top][index]
                for index 
                in range(left , right + 1)
            ]
            top += 1

            result += [
                matrix[index][right]
                for index 
                in range(top , bottom + 1)
            ]
            right -= 1

            if top <= bottom : 

                result += [
                    matrix[bottom][index]
                    for index 
                    in range(right , left - 1 , -1)
                ]
                bottom -= 1

            if left <= right : 

                result += [
                    matrix[index][left]
                    for index
                    in range(bottom , top - 1 , -1)
                ]
                left += 1

        return result
        
