# <-----------METHOD 1----------->

class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_len = min([
            len(val)
            for val 
            in strs
        ])
        
        strss = [
            val[:min_len]
            for val 
            in strs
        ]

        lc = ''

        for index in range(min_len):

            counter = 0

            pivot = strss[0][index]
            
            for val in strss:

                if val[index] == pivot : counter += 1

            if counter == len(strss) : lc += pivot
            else : break

        return lc

# <-----------METHOD 2----------->

class Solution:
    
    def longestCommonPrefix(self, v: List[str]) -> str:
        
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        
        for i in range(min(len(first),len(last))):
            
            if(first[i]!=last[i]) : return ans
            
            ans+=first[i]
        
        return ans 
