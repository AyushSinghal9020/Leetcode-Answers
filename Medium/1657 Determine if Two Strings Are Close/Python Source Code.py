class Solution:
    
    def closeStrings(self, word1: str, word2: str) -> bool:

        frequency_1 = {}
        frequency_2 = {}

        for val in word1 : 
            
            if val in frequency_1.keys() : frequency_1[val] += 1
            else : frequency_1[val] = 1
        
        for val in word2 : 
            
            if val in frequency_2.keys() : frequency_2[val] += 1
            else : frequency_2[val] = 1

        freqv_1 = sorted(list(frequency_1.values()))
        freqv_2 = sorted(list(frequency_2.values()))
        freqk_1 = sorted(list(frequency_1.keys()))
        freqk_2 = sorted(list(frequency_2.keys()))

        if (freqv_1 == freqv_2) and (freqk_1 == freqk_2): return True
        return False
