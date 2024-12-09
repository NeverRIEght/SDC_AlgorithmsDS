from collections import defaultdict
from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Double DFS with memoization
        # O(n)
        graph = defaultdict(list)
        for source, target in edges: # undirected graph
            graph[source].append(target)
            graph[target].append(source)

        dist = [0] * n  # sum of distances to all other nodes
        size = [1] * n  # subtree size including itself

        # Calculate subtree size and sum of distances for each node
        def dfs1(node, parent):
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs1(neighbor, node)
                    size[node] += size[neighbor]
                    dist[node] += dist[neighbor] + size[neighbor]
        # Recalculate sum of distances for each node
        # Take into account the size of the subtree of the current node and it's position in the tree
        def dfs2(node, parent):
            for neighbor in graph[node]:
                if neighbor != parent:
                    dist[neighbor] = dist[node] - size[neighbor] + (n - size[neighbor])
                    dfs2(neighbor, node)

        dfs1(0, -1)
        dfs2(0, -1)

        return dist