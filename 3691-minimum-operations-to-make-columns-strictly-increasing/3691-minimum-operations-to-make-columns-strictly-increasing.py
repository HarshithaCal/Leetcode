class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:

        n_cols = len(grid[0])
        n_rows = len(grid)
        n_ops = 0
    
        for col in range(n_cols):
            prev = grid[0][col]
            for row in range(1, n_rows):
                curr = grid[row][col]
                if curr <= prev:
                    # Calculate the increment needed to make the current element greater than `prev`
                    increment = prev - curr + 1
                    n_ops += increment
                    grid[row][col] = prev + 1  # Update the grid with the adjusted value
                else:
                    grid[row][col] = curr  # No adjustment needed
    
                # Update `prev` for the next iteration
                prev = grid[row][col]
    
        return n_ops
                    

        