class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = 'aeiouAEIOU'
        vow = [
            val 
            for val 
            in s
            if val in vowels
        ]

        t = ''
        for index in range(len(s)):
            
            if s[index] in vowels : 
                t += str(vow[-1])
                vow.pop(-1)
            
            else : t += s[index] 
        
        return t
