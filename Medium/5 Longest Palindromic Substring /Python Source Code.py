class Solution:
    
    def longestPalindrome(self, s: str) -> str:

        maxi = ''
        
        def check_palindrome(string):

            if string[::-1] == string : return True 
            return False 


        for start_index in range(len(s)):

            for end_index in range(start_index , len(s)):

                window = s[start_index  : end_index + 1]

                if check_palindrome(window):

                    if len(window) > len(maxi) : maxi = window

        
        return maxi
        
