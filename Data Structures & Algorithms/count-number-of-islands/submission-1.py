class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        output = 0 
        self.landscape = grid.copy()
        row_count = len(self.landscape)
        col_count = len(self.landscape[0])

        for row in range(len(self.landscape)):
            for col in range(len(self.landscape[0])):
                if self.landscape[row][col] == '1':
                    self.dfs(row, col, row_count, col_count)
                    output += 1
        
        return output
    
    def dfs(self, row, col, row_count, col_count):
        if row not in range(row_count) or col not in range(col_count):
            return
        if self.landscape[row][col] == '0':
            return 
        if self.landscape[row][col] == '1':
            self.landscape[row][col] = '0'
            self.dfs(row + 1, col, row_count, col_count)
            self.dfs(row - 1, col, row_count, col_count)
            self.dfs(row, col + 1, row_count, col_count)
            self.dfs(row, col - 1, row_count, col_count)
        






        
