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
            visited.add(course)
            if not course in adj_list:
                # no prereqs
                visited.remove(course)
                return True
            for prereq in adj_list[course]:
                if prereq in visited:
                    # there must be a cycle since we already saw the prereq
                    # yet we are visiting it again on this run of dfs
                    visited.remove(course)
                    return False
                if not dfs(prereq):
                    # if we can't get the prereq, we cant get the course
                    visited.remove(course)
                    return False
            # otherwise, we can get the course
            visited.remove(course)
            adj_list[course] = []
            return True

        # check if each course can be completed
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True