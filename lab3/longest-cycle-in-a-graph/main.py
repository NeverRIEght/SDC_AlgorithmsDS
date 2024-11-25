from collections import defaultdict, deque
from typing import List

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        # define graph
        # key = node, value = list of its neighbors
        graph = defaultdict(list)
        start = 0
        for end in edges:
            if end != -1: # in case edge exists
                graph[start].append(end)
            start += 1

        # key = node, value = number of times visited
        visited = {}
        longest_cycle = -1

        def dfs(node, step):
            nonlocal longest_cycle
            if node in visited:
                if visited[node] >= 0:
                    cycle_length = step - visited[node]
                    longest_cycle = max(longest_cycle, cycle_length)
                return

            visited[node] = step

            for neighbor in graph[node]:
                dfs(neighbor, step + 1)

            # Remove binding to prevent further checks
            visited[node] = -1

        # for each non-visited node, perform cycle check
        for node in range(len(edges)):
            if node not in visited:
                dfs(node, 0)

        return longest_cycle