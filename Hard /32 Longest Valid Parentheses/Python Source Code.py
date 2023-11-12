class Solution:
    
    def longestValidParentheses(self, s: str) -> int:
        
        max_length = 0
                
        left , right = 0 , 0        

        for index in range(len(s)):
            
            if s[index] == '('  : left += 1
            else : right += 1                        
            
            if left == right : max_length = max(max_length , left * 2)
            elif right > left : left , right = 0 , 0
        
        left , right = 0 , 0        
        
        for index in range(len(s) - 1 , - 1 , - 1) :
            
            if s[index] == '(' : left += 1
            else : right += 1            
            
            if left == right : max_length = max(max_length , left * 2)
            elif left > right : left , right = 0 , 0
        
        return max_length
