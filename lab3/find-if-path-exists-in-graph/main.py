class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        visited = set()
        def dfs(node):
            if node == destination:
                return True
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited: # if neighbour is not visited
                    if dfs(neighbour): # and it's value is equal to destination
                        return True
            return False

        return dfs(source)