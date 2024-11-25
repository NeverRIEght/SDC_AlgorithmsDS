class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # 0 - not visited
        # 1 - group 1
        # 2 - group 2

        groups = [0] * len(graph)

        def dfs(node, group):
            if groups[node] != 0:
                return groups[node] == group

            groups[node] = group
            for neighbor in graph[node]:
                if not dfs(neighbor, 3 - group):
                    return False

            return True

        for i in range(len(graph)):
            if (groups[i] == 0 # if not visited
                    and not dfs(i, 1) # and the color is wrong
            ):
                return False # then it's not bipartit

        return True