class Solution:
    
    def intToRoman(self, num: int) -> str:

        rt = ''

        while num != 0 : 
            
            if num >= 1000 :
                num -= 1000
                rt += 'M'
            
            elif num >= 900 : 
                num -= 900
                rt += 'CM'
            
            elif num >= 500 :
                num -= 500
                rt += 'D'
            
            elif num >= 400 : 
                num -= 400 
                rt += 'CD'
            
            elif num >= 100 :
                num -= 100
                rt += 'C'
            
            elif num >= 90 :
                num -= 90
                rt += 'XC'
            
            elif num >= 50 : 
                num -= 50 
                rt += 'L'
            
            elif num >= 40 :
                num -= 40 
                rt += 'XL'
            
            elif num >= 10 :
                num -= 10 
                rt += 'X'
            
            elif num >= 9 : 
                num -= 9
                rt += 'IX'
            
            elif num >= 5 :
                num -= 5
                rt += 'V' 
            
            elif num >= 4 :
                num -= 4
                rt += 'IV'
            
            else : 
                num -= 1
                rt += 'I'

        return rt
