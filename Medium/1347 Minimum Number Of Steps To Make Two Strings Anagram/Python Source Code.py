import collections

class Solution:
    
    def minSteps(self, s: str, t: str) -> int:
        
        S, T = map(collections.Counter, (s, t))
        
		return sum(count for count in (T - S).values())
