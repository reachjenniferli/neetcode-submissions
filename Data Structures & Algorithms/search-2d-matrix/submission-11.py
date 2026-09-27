class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix)
        
        while l < r-1: 
            m = l + (r-l)//2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] > target:
                r = m-1
            else:
                l = m
        
        row = l
        l, r = 0, len(matrix[row])
        
        while l < r:
            m = l + (r-l)//2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m
            else:
                l = m+1

        return False