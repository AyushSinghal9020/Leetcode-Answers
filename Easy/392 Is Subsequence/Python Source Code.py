# <-------------METHOD 1------------->


class Solution:
    
    def isSubsequence(self, s: str, t: str) -> bool:

        r = []
        s = list(s)
        t = t

        for s_index in range(len(s)):

            for t_index in range(len(t)):

                if s[s_index] == t[t_index]: r.append(t_index)

        if sorted(r) == r and (len(list(set(r))) >= len(s)): return True
        return False

# <-------------METHOD 2------------->

class Solution:
    
    def isSubsequence(self, s: str, t: str) -> bool:

        i, j = 0, 0
        
        while i < len(s) and j < len(t):
            
            if s[i] == t[j]:i += 1
            j += 1
       
        return i == len(s)

        
        
