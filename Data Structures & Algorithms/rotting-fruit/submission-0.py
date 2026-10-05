class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh, minute = 0, 0
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        # bfs
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while q and fresh > 0:
            for _ in range(len(q)):
                rot_row, rot_col = q.popleft()
                for row_change, col_change in directions: 
                    r = rot_row + row_change
                    c = rot_col + col_change
                    if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r, c))
            minute += 1
        
        if fresh > 0:
            return -1
        return minute








