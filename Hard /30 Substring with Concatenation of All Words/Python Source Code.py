# <-------------METHOD 1------------->

class Solution:
    
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        str_split = lambda string , window : [
            string[index : index + window]
            for index 
            in range(0 , len(string) , window)
        ]

        def checker(list_1 , list_2):

            list_1 = sorted(list_1)
            list_2 = sorted(list_2)

            while list_1 != [] :

                if list_1[0] == list_2[0] : 
                    list_1.pop(0)
                    list_2.pop(0)

                else: return None

            return True

        window_size = len(words) * len(words[0])
        rt = []

        for index in range(len(s) - window_size + 1):

            window = s[index : index + window_size]

            different_words = str_split(window , len(words[0]))

            if checker(different_words , words): rt.append(index)

        return rt

# <-------------METHOD 2------------->

class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        def calc(index , susbstr_len):

            counter = 0
            
            while (index < index + substr_len):
                
                news = s[index : index + word_length]
                
                if news in self.global_dictionary :
                    
                    self.global_dictionary[news] -= 1 
                    
                    if self.global_dictionary[news] == 0 : counter += 1 
                    
                    index += word_length
                
                else : return False 
            
            if counter == len(self.global_dictionary) : return True 
            return False
        
        word_length = len(words[0])

        store_dict = {}
        
        for value in words :
            
            if value in store_dict : store_dict[value] += 1 
            else : store_dict[value] = 1 

        substr_len = len(words)*len(words[0])
        
        return_val = []
        index = 0
        
        while(index < len(s) - substr_len + 1):
            
            self.global_dictionary = {x : store_dict[x] for x in store_dict}
            
            if calc(index , substr_len) :
                
                return_val += [index]
                index += 1
            
            else : index += 1
        
        return return_val 
