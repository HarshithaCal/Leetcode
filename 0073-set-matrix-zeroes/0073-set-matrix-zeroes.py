class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ##not the most optimal solution in terms of the space usage.
        horizontal = [0] * len(matrix[0])
        vertical = [0] * len(matrix)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    horizontal[c] = 1
                    vertical[r] = 1
        print(vertical, "\n", horizontal)

        for i in range(len(vertical)):
            for j in range(len(horizontal)):
                if horizontal[j]==1 or vertical[i] == 1:
                    matrix[i][j]= 0
        print(matrix)


        