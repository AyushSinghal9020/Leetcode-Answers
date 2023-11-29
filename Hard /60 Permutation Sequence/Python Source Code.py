class Solution:
    
    def getPermutation(self, n: int, k: int) -> str:

        total = 1
        ret = ''
        digits = [
            val 
            for val 
            in range(1 , n + 1)
        ]
        
        for val in range(2 , n) : total *= val
        
        k -= 1

        for value in range(n-1, -1, -1):
            
            val = k // total
            ret += str(digits[val])
            k -= val * total
            
            del digits[val]
            

            if value > 0 : total //= value 

        return ret

