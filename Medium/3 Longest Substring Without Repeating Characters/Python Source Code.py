# <-----------METHOD 1----------->

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 1 : return 1 
        if len(s) == 0 : return 0

        def check_unique_chars(string):

            if len(set(string)) == len(string): return True 
            return False

        maxi = 0

        for start_index in range(len(s)):

            for end_index in range(start_index  , len(s) + 1):

                window = s[start_index : end_index]

                if check_unique_chars(window) : 
                    print('haha' , window , len(window))
                    if len(window) > maxi : maxi = len(window)

            
        return maxi        

# <-----------METHOD 2----------->

class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0
        
        for right in range(n):
            
            if s[right] not in charSet:
                
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            
            else:
                
                while s[right] in charSet:
                    
                    charSet.remove(s[left])
                    left += 1
                
                charSet.add(s[right])
        
        return maxLength
