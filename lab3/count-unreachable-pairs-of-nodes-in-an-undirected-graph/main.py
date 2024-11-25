from collections import defaultdict, deque

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # key = node, value = list of its neighbors
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited_nodes = [False] * n
        component_sizes = []

        def bfs_count_connected_nodes(start):
            q = deque([start])
            visited_nodes[start] = True
            size = 0

            while q:
                node = q.popleft()
                size += 1
                for neighbor in graph[node]:
                    if not visited_nodes[neighbor]:
                        visited_nodes[neighbor] = True
                        q.append(neighbor)
            return size

        # Look through all nodes
        # For each unique node, count the number of connected nodes
        for i in range(n):
            if not visited_nodes[i]:
                component_sizes.append(bfs_count_connected_nodes(i))

        total_pairs = n * (n - 1) // 2

        reachable_pairs = 0
        for k in component_sizes:
            reachable_pairs += k * (k - 1) // 2

        unreachable_pairs = total_pairs - reachable_pairs

        return unreachable_pairs
