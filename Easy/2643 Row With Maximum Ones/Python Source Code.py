class Solution:
    
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        
        y = [sum(row) for row in mat]
        
        maxi = 0
        ind = 0
        
        for index , i in enumerate(y):
            
            if i > maxi: 
                
                maxi = i
                ind = index


        return [ind , maxi]
