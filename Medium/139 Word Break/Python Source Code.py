class Solution:
    
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        
        i = 0
        
        def func(x , wordDict , value):
            
            if value == len(wordDict) : 
                
                return True
            
            elif wordDict[value] in x:
                
                a = x[x.index(wordDict[value][-1]) + 1:]
                
                return func(a , wordDict , value + 1)
            
            else:
                
                return False

        func(s , wordDict , 0)
