class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0 
        self.landscape = grid.copy()
        row_count = len(self.landscape)
        col_count = len(self.landscape[0])

        for row in range(len(self.landscape)):
            for col in range(len(self.landscape[0])):
                if self.landscape[row][col] == 1:
                    max_area = max(max_area, self.dfs(row, col, row_count, col_count))
        
        return max_area
    
    def dfs(self, row, col, row_count, col_count):
        if row not in range(row_count) or col not in range(col_count):
            return 0
        if self.landscape[row][col] == 0:
            return 0 
        if self.landscape[row][col] == 1:
            self.landscape[row][col] = 0
            return 1 + self.dfs(row + 1, col, row_count, col_count) + self.dfs(row - 1, col, row_count, col_count) + self.dfs(row, col + 1, row_count, col_count) + self.dfs(row, col - 1, row_count, col_count)
        



