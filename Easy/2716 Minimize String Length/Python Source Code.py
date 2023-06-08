class Solution:
    
    def minimizedStringLength(self, s: str) -> int:
        
        vocab = []
        
        for i in s :
            
            if i not in vocab:
                
                vocab.append(i) 

        return len(vocab)
