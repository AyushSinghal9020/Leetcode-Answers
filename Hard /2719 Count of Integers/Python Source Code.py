# BRUTE FORCE

class Solution:
    
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        
        count = 0
        
        for i in range(int(num1) , int(num2)):
            
            it = sum(int(j) for j in str(i))
            
            if it >= min_sum and it <= max_sum:
                
                count += 1
