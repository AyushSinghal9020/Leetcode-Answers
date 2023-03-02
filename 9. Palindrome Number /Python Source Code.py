class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        z = [list(str(input))[-i] 
             for i in range (1 , len(list(str(input))) + 1)]
        
        sample_str = ""
        
        for j in z: sample_str += j
        
        try :
        
            if input == int(sample_str): 
                
                return True
        
            else : 
                
                return False
        
        except : 
            
            return False
