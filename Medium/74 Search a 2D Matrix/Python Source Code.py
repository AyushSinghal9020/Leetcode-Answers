class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            out_list = []
            for i in matrix :
                if target in i : out_list.append("True")
                else:out_list.append("False")

            if "True" in out_list:return True
            else: return False
