class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {} # adjacency list
        order = [] # result
        visited = set()
        cycle = set()

        # build adjacency list
        # key: course, value: list of prereqs
        for i in range(numCourses):
            graph[i] = []

        for i in range(len(prerequisites)):
            a = prerequisites[i][1]
            b = prerequisites[i][0]
            graph[b].append(a)
        
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            cycle.add(node)
            for prereq in graph[node]: 
                if not dfs(prereq):
                    return False
            cycle.remove(node)
            visited.add(node)
            order.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return order

        