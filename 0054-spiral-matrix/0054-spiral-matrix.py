class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #TC - O(m*n) - every element is visited exactly
        m, n = len(matrix), len(matrix[0])
        res = []
        left = 0; right = (n-1); top = 0; bottom = (m-1)

        while top<= bottom and left<=right:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top+=1   

            for i in range(top, bottom+1):
                res.append(matrix[i][right])
                print(matrix[i][right])
            right -= 1
            
            if top<= bottom:
                for i in range(right, left-1, -1):
                    print("right, left ", right, left-1)
                    res.append(matrix[bottom][i])
                    print(matrix[bottom][i])
                bottom -= 1
            
            if left <=right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                    print(matrix[i][left])

                left+=1 
        return res
            

