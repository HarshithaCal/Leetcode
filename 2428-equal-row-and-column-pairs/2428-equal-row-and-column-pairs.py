class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        #optimized: TC - O(n^2)
        # Store rows as tuples. Tuples are immutable and hashable so faster.
        rows = [tuple(row) for row in grid]

        n = len(grid)
        # Transpose the matrix to get columns as tuples
        cols = [tuple(grid[i][j] for i in range(n)) for j in range(n)]
        
        # Count matching row-column pairs
        count = 0
        for row in rows:
            count += cols.count(row)
        
        return count



        # #Brute-force: Transpose and check - TC - O(n^3)

        # n = len(grid)
        # count = 0

        # # Compare each row with each column
        # for i in range(n):
        #     for j in range(n):
        #         if all(grid[i][k] == grid[k][j] for k in range(n)):
        #             count += 1
        
        # return count
        