class Solution:
    
    def countAndSay(self, n: int) -> str:
        
        if n==1 : return "1"
        
        x = self.countAndSay(n-1)
        y = x[0]
        
        s = ""
        ct=1
        
        for index in range(1 , len(x)):
            
            if x[index] == y : ct += 1
            else:
                
                s += str(ct)
                s += str(y)
                
                y = x[index]
                ct = 1
        
        s += str(ct)
        s += str(y)
        
        return s
