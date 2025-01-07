class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS, since we are searching for a destination (cycle)
        # O(n * m),
        # n = number of courses
        # m = number of prerequisites for each course

        # HashMap: course -> list of its prerequisites
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # Statuses for each node:
        # 0 = not visited
        # 1 = in progress, trying to find a cycle
        # 2 = processed
        status = [0] * numCourses


        # Depth-first search
        # True = no cycle
        # False = cycle found
        def dfs(course):
            # Already processed
            if status[course] == 2:
                return True

            # Mark node as "in progress" and check prerequisites
            if status[course] == 1:
                return False
            status[course] = 1
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            # If there is no cycle, mark node as processed
            status[course] = 2
            return True

        # Check all courses
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True