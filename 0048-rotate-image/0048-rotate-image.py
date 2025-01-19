class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ### vertical reversal
        top = 0
        bottom = len(matrix) -1

        while top < bottom:
            for col in range(len(matrix)):
                matrix[top][col], matrix[bottom][col] = matrix[bottom][col], matrix[top][col]
            top+= 1
            bottom -= 1
        
        ### transpose
        for row in range(len(matrix)):
            for col in range(row+1, len(matrix)):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        return matrix
        

        


        