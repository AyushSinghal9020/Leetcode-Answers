class Solution:
    def twoSum(self, s, t):
        for i in range(0 , len(s)):
            for j in range(0, len(s)):
                if i != j:
                    if s[i] + s[j] == t:
                        if i in o:
                            continue
                        else :
                            o.append(i)
                        if j in o:
                            continue
                        else : 
                            o.append(j)
        return o
