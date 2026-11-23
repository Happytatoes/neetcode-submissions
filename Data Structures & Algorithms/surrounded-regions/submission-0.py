class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        # idea: mark O as safe if
        # we can reach them from the edge
        # then, turn every other O into an X

        ROWS, COLS = len(board), len(board[0])
        safe = set()

        def dfs(r, c):
            if board[r][c] != 'O':
                return
            safe.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for i in range(len(directions)):
                new_row = r + directions[i][0]
                new_col = c + directions[i][1]
                if (new_row, new_col) in safe:
                    continue
                if new_row < 0 or new_row >= ROWS or new_col < 0 or new_col >= COLS:
                    continue
                dfs(new_row, new_col)
            
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS): 
                if (r, c) not in safe and board[r][c] == 'O':
                    board[r][c] = 'X'
