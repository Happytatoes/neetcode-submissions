class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = {}
        return self.recurse(0, 0, m, n)


    def recurse(self, m, n, rows, cols):

        if (m, n) in self.memo:
            return self.memo[(m, n)]

        if (m == rows - 1 and n == cols - 1) or (m == rows - 1) or (n == cols - 1):
            return 1

        result = self.recurse(m + 1, n, rows, cols) + self.recurse(m, n + 1, rows, cols)  
        self.memo[(m, n)] = result
        return result
