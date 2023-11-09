class Solution:
    
    def romanToInt(self, s: str) -> int:

        special_romans = ['IV' , 'IX' , 'XL' , 'XC' , 'CD' , 'CM']
        romans = ['I' , 'V' , 'X' , 'L' , 'C' , 'D' , 'M']

        rt = 0
        index = 0

        while index < len(s):

            window = s[index : index + 2]
                
            if window in special_romans : 
                if window == special_romans[0] : rt += 4
                elif window == special_romans[1] : rt += 9
                elif window == special_romans[2] : rt += 40
                elif window == special_romans[3] : rt += 90
                elif window == special_romans[4] : rt += 400
                elif window == special_romans[5] : rt += 900

                index += 2

            else : 

                window = s[index]

                if window == romans[0] : rt += 1
                elif window == romans[1] : rt += 5
                elif window == romans[2] : rt += 10
                elif window == romans[3] : rt += 50
                elif window == romans[4] : rt += 100
                elif window == romans[5] : rt += 500
                elif window == romans[6] : rt += 1000

                index += 1

        return rt

            
