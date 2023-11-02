class Solution:
    
    def compress(self, chars: List[str]) -> int:
        
        look_up = []
        counter = 1
        
        for index in range(1 , len(chars)):
            
            if chars[index] == chars[index - 1] : counter += 1
            else:
                look_up.append([chars[index - 1] , counter])
                counter = 1
        
        look_up.append([chars[-1] , counter]) 
        index = 0
        
        for val_1 , val_2 in look_up :
            
            chars[index] = val_1
            index += 1
            
            if val_2 > 1 :
                
                for item in str(val_2) :
                    
                    chars[index] = str(item)
                    index += 1
        
        return index
