class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])    
        island_count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    island_count += 1
                    self.dfs(grid, row, col, rows, cols)  # sink this whole island

        return island_count

    def dfs(self, grid, row, col, rows, cols):
        # out of bounds, or water, or already visited -> stop
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != '1':
            return
        
        # turn the one into a zero
        grid[row][col] = '0'
        
        self.dfs(grid, row + 1, col, rows, cols)
        self.dfs(grid, row - 1, col, rows, cols)
        self.dfs(grid, row, col + 1, rows, cols)
        self.dfs(grid, row, col - 1, rows, cols)


