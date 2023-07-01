class Solution:
    
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        
        time = arrivalTime + delayedTime
        
        if float(time) >= float(24):time -= 24
        
        return time
