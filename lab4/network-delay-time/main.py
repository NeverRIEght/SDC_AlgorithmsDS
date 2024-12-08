from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        root = k
        nodes_count = n

        # numbers of nodes, which are processed
        visited = set()
        # distances to root. n+1 is used to assign node numbers to list indices, 0 element will be empty
        distances = [float('inf')] * (nodes_count + 1)

        # distance to root is zero
        distances[root] = 0

        while len(visited) < nodes_count:
            current_node = -1
            current_distance = float('inf')
            for source, target, time in times:
                if source not in visited and distances[source] < current_distance:
                    current_node = source
                    current_distance = distances[source]

            if current_node == -1:
                break

            visited.add(current_node)

            for source, target, time in times:
                if source == current_node and target not in visited:
                    new_distance = distances[current_node] + time
                    if new_distance < distances[target]:
                        distances[target] = new_distance

        # delete first element, since it's not used
        del distances[0]

        for d in range(len(distances)):
            if distances[d] == float('inf'):
                return -1

        return max(distances)


print(Solution().networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
