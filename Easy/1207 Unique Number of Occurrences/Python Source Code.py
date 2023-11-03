class Solution:
    
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        frequency = {}

        for val in arr:
            
            if val in frequency.keys() : frequency[val] += 1
            else : frequency[val] = 1

        if sorted(list(set(list(frequency.values())))) == sorted(list(frequency.values())): return True 
        return False
        
