class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range (num+1):
            list = []
            k = 0
            for j in str(i):
                list.append(j)
            for l in list:
                k = k + int(l)
            if k % 2 == 0:       
                count = count + 1
        return count
