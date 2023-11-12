class Solution:
    ans=[]
    def solve(self,array,Sum,candidates,target,start):
        if Sum==target:
            self.ans.append(array)
        for index in range(start,len(candidates)):
            i=candidates[index]
            if Sum+i>target:
                return
            array1=list(array)
            array1.append(i)
            Sum1=Sum+i
            self.solve(array1,Sum1,candidates,target,index)
    
        

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans=[]
        candidates.sort()
        self.solve([],0,candidates,target,0)

        return self.ans
        
        
