class Solution:
    
    def mergeAlternately(self, word1: str, word2: str) -> str:

        stri = ''
        
        for x , y in zip(word1 , word2):
        
            stri += x
            stri += y

        if len(word1) > len(word2):stri += word1[len(word2) : ]
        elif len(word2) > len(word1):stri += word2[len(word1) : ]

        return stri
