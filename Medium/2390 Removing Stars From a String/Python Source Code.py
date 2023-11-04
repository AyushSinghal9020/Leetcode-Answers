class Solution:
    
    def removeStars(self, s: str) -> str:

        stack = []
        stri = ''
        
        for val in s:
            
            stack.append(val)
            
            if val == '*':
                
                stack.pop(-1)
                stack.pop(-1)

        for val in stack:
            
            stri += val

        return stri
