class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        i = r // 2
        row = -1

        for count in range(int(len(matrix)/2)+1):
            if matrix[i][0] <= target:
                if matrix[i][len(matrix[i])-1] >= target:
                    row = i
                    break
                l = i
                i = (r - l) // 2 + l 
            elif matrix[i][-1] >= target:
                r = i
                i = (r - l) // 2 + l 
        
        #print(row)
        #print(matrix[row])
        l, r = 0, len(matrix[row])-1
        i = r // 2
        for count in range(len(matrix[row])//2+1):
            #print(matrix[row][i])
            #print(matrix[row][l])
            #print(matrix[row][r])
            #print("__")
            if matrix[row][l] == target:
                return True
            elif matrix[row][r] == target:
                return True
            if matrix[row][i] < target:
                l = i
                i = ((r - l) // 2) + l 
            elif matrix[row][i] > target:
                r = i
                i = ((r - l) // 2) + l 
            else: 
                return True
            

        return False




