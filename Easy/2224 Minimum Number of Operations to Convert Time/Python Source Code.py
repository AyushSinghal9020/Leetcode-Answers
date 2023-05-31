class solution:
    def answer(self, current_time, correct_time, count  = 0) :

        a = current_time.rsplit(":")
        b = correct_time.rsplit(":")

        current_time = ((int(a[0]))*60) + int(a[1])
        correct_time = ((int(b[0]))*60) + int(b[1])
    
        difference = correct_time - current_time
    
        if difference == 0:
            return count

        else :
            while(difference != 0):
                if difference>= 60:
                    difference = difference - 60
                    count  = count + 1
        
                elif difference>= 15:
                    difference = difference - 15
                    count = count + 1
        
                elif difference>= 5:
                    difference = difference - 5
                    count  = count + 1
        
                elif difference>= 1:
                    difference = difference - 1
                    count = count + 1
            return count 
