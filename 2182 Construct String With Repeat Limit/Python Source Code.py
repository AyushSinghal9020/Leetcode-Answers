class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:

        list = []
        output = ''

        for i in s:

            list.append(i)

        list.sort()

        for j in range(len(list)) :

            if j < len(list) - 1:

                if list[j] != list[j+1]:

                    continue

                else :

                    count = 0 

                    while count <= 3:

                        count = count + 1

                        if count <= repeatLimit:

                            list.append(list[j])
                            list.remove(list[j])

            else :

                break


        for element in list:
            output += element
