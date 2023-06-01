class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31 or (-x) <= -(2**31):
            return 0
        else : 
            y = list(str(x))
            z = []

            for i in range(1 , len(y) + 1):

                z.append(y[-i])

            while 0 in z:

                z = z.remove(0)

            if z[-1] == "-":

                z.pop(-1)
                str1 = ""
                z = int(str1.join(z))
                z = -z

            else:

                str1 = ""
                z = int(str1.join(z))
        
            return z
