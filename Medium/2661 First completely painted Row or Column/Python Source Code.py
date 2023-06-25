class Solution:
    
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        
        mat_t = []
        
        for i in range(len(mat[0])):
            
            mat_x = []
            
            for j in range(len(mat)):mat_x.append(mat[j][i])
            
            mat_t.append(mat_x)

        for index , i in enumerate(arr):
            
            for _ in mat:if i in _:_.remove(i)
            for _ in mat_t:if i in _:_.remove(i)
            if [] in mat or [] in mat_t:
                return index
