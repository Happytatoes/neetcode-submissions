class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        if n == 0:
            return 0

        visited = set()
        graph = {}
        
        # build adjacency list
        for i in range(n):
            graph[i] = []
        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for adj in graph[node]:
                dfs(adj)

        res = 0
        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            res += 1
        return res
        
            