class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = {}
        visited = set()

        # build adjacency list
        for pair_index in range(len(prerequisites)):
            if prerequisites[pair_index][0] in adj_list:
                adj_list[prerequisites[pair_index][0]].append(prerequisites[pair_index][1])
            else:
                adj_list[prerequisites[pair_index][0]] = [prerequisites[pair_index][1]]

        def dfs(course):
            # no prereqs
            if not course in adj_list:
                return True
            
            # remove before return so the visited set 
            # is only for the active recursion path
            visited.add(course)
            for prereq in adj_list[course]:
                if prereq in visited:
                    visited.remove(course)
                    return False
                if not dfs(prereq):
                    visited.remove(course)
                    return False
            visited.remove(course)

            # remove the course from the adj list so we dont compute it again
            adj_list[course] = []
            return True

        # check if each course can be completed
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True