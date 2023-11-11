class Solution:
    
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
    
        def dp(val_1 : int , val_2 : int) -> bool :
            
            if (val_1 , val_2) in memo : return memo[(val_1, val_2)]
            if val_2 == len(p) : return val_1 == len(s)
        
            first_match = (val_1 < len(s)) and (p[val_2] == s[val_1] or p[val_2] == '.')
        
            if val_2 + 1 < len(p) and p[val_2+1] == '*' : ans = dp(val_1, val_2+2) or (first_match and dp(val_1+1, val_2))
            else : ans = first_match and dp(val_1+1, val_2+1)
        
            memo[(val_1 , val_2)] = ans
            return ans
    
        return dp(0, 0)
