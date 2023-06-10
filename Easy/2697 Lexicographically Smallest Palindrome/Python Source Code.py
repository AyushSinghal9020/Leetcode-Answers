class Solution:
    
    def makeSmallestPalindrome(self, s: str) -> str:
        
        if len(s)%2 == 0:
            
            if len(s) == 2:
                
                s = min(s) * 2
            
            else:
                
                l = s[:int(len(s)/2)] + s[:int(len(s)/2)][::-1]
                k = s[:int(len(s)/2)][::-1] + s[:int(len(s)/2)]
                
                if k[0] < l[0]:
                    
                    s = k
                
                else:
                    
                    s = l 
        
        else:
            
            l = s[(len(s)//2) + 1:][::-1] + s[len(s)//2] + s[(len(s) // 2 + 1):]
            k = s[:(len(s)//2)] + s[len(s)//2] + s[:len(s) // 2][::-1]
            
            if k[0] < l[0]:
                
                s = k
            
            else:
                
                s = l

        return s
