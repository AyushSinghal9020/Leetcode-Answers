class Solution:
    
    def divide(dividend : int , divisor : int) -> int:
    
        quotient = 0
    
        if dividend == divisor : 
    
            return 1
    
        if dividend == -divisor :
    
            return -1
    
        elif divisor < 0 :
    
            divisor = -divisor
    
            while dividend > divisor : 
    
                dividend -= divisor
                quotient -= 1
    
            return quotient

        else :
    
            while dividend > divisor : 
    
                dividend -= divisor
                quotient += 1
    
            return quotient
