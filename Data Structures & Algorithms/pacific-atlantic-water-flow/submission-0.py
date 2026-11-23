class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(coords, target, visited): 

            print(coords)

            target.add(coords)
            visited.add(coords)
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for i in range(len(directions)):
                new_row = coords[0] + directions[i][0]
                new_col = coords[1] + directions[i][1]
                if (new_row, new_col) in visited:
                    continue 
                if new_row < 0 or new_row >= ROWS or new_col < 0 or new_col >= COLS:
                    continue 
                if heights[new_row][new_col] < heights[coords[0]][coords[1]]:
                    continue
                dfs((new_row, new_col), target, visited)
                
        # dfs starting from the oceans
        # seeing if we can get to a cell
        for r in range(ROWS):
            dfs((r, 0), pac, set())
            dfs((r, COLS - 1), atl, set())

        for c in range(COLS):
            dfs((0, c), pac, set())
            dfs((ROWS - 1, c), atl, set())

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res