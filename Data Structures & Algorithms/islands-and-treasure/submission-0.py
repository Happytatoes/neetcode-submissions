class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, cols = len(grid), len(grid[0])
        q = deque()
        iteration = 1
        
        for r in range(rows):
            for c in range(cols):            
                if grid[r][c] == 0:
                    q.append((r, c))

        while q and len(q) > 0:
            # this iteration of bfs
            for _ in range(len(q)):
                row, col = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for d in directions:
                    r = row + d[0]
                    c = col + d[1]
                    if 0 <= r and r < rows and 0 <= c and c < cols:
                        if grid[r][c] == 2147483647:
                            grid[r][c] = iteration
                            q.append((r, c))
            iteration += 1
