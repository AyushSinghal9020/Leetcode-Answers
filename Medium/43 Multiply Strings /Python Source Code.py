# <--------METHOD 1-------->

class Solution:
    
    def multiply(self, num1: str, num2: str) -> str:
        
        return str(eval(num1+'*'+num2))     

# <--------METHOD 2-------->

class Solution:

    def multiply(self, num1: str, num2: str) -> str:

        if num1 == '0' or num2 == '0' : return '0'

        num1 = num1[::-1]
        num2 = num2[::-1]

        col = []
        
        for val in num1 : 

            carry = 0   
            row = []

            for value in num2 : 

                multiplied_value = int(val) * int(value)

                if carry != 0 : 

                    multiplied_value +=  carry

                    carry = 0  

                multiplied_value = str(multiplied_value)

                if len(multiplied_value) > 1 : 
                    
                    carry = int(multiplied_value[:-1])
                    row.append(int(multiplied_value[-1]))
                
                else : row.append(int(multiplied_value))

            carry = int(carry)
            
            if carry != 0 : row.append(int(carry))

            col.append(row)

        col = [val[::-1]for val in col]
        for index in range(len(col)) : col[index] += [0] * index

        col = [val[::-1] for val in col]

        max_len = 0

        for val in col : 
            if len(val) > max_len : max_len = len(val)

        for val in col : val += [0] * (max_len - len(val))

        l_list = []

        for index in range(max_len) : 

            add_val = []

            for val in col : 

                if index < len(val) : add_val.append(val[index])
                else : break 

            l_list.append(add_val)

        l_list.reverse()

        add_vals = [sum(val) for val in l_list]
        add_vals.reverse()

        rt = []

        carry = 0

        for val in add_vals :

            if carry != 0 : 

                val += carry 
                carry = 0

            value = str(val)

            if len(value) > 1 : 
                
                carry = int(value[:-1])

                val = int(value[-1])

                rt.append(val)

            else : rt.append(val)

        if carry != 0 : rt.append(carry)

        rt.reverse()

        t = ''

        for val in rt : t += str(val)

        return t
