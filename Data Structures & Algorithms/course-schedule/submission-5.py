class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = {}
        visited = set()

        # build adjacency list
        for i in range(len(prerequisites)):
            course = prerequisites[i][0]
            prereq = prerequisites[i][1]
            if course not in adj_list:
                adj_list[course] = []
            adj_list[course].append(prereq)

        def dfs(course):
            # no prereqs
            if not course in adj_list:
                return True
            
            visited.add(course)
            for prereq in adj_list[course]:
                # we've already seen this course
                # cycle detected, it's impossible
                if prereq in visited:
                    visited.remove(course)
                    return False
                # it fails in the future 
                if not dfs(prereq):
                    visited.remove(course)
                    return False
            
            # remove the course from the adj list so we dont compute it again
            adj_list[course] = []
            visited.remove(course)
            return True

        # check if each course can be completed
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True