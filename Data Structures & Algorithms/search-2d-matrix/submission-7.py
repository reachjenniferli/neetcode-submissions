class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = 0
        R = len(matrix)-1
        M = (R-L) // 2
        row = -1

        if target <= matrix[0][0]:
            if target < matrix [0][0]:
                return False
            else:
                return True

        elif target >= matrix[len(matrix)-1][0]:
            if target > matrix[len(matrix)-1][0]:
                row = len(matrix)-1
            else:
                return True

        while row == -1:
            #print(L)
            #print(M)
            #print(R)
            curr = matrix[M][0]
            #print(curr)
            #print("_____")
            if curr == target:
                return True
            if L == M:
                row = M
            if curr > target:
                R = M
            elif curr < target:
                L = M

            M = (R-L)//2 + L

        L = 0
        R = len(matrix[row])-1
        M = (R-L) // 2

        if matrix[row][R] == target:
            return True
        
        while M != R and M != L:
            curr = matrix[row][M]

            if curr == target:
                return True

            elif curr > target:
                R = M

            elif curr < target:
                L = M

            M = (R-L) // 2 + L

        return False