class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if n == 0:
            return True

        # idea: if we traverse from one node
        # we should get the exact visited set with 
        # no cycles or unreachable nodes

        visited = set()
        graph = {}
        
        # build adjacency list
        for i in range(n):
            graph[i] = []
        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
        
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for adj in graph[node]:
                if adj == prev:
                    continue
                if not dfs(adj, node):
                    return False
            return True

        return dfs(0, -1) and n == len(visited)
        
            