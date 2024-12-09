class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Kruskal's algorithm with Union-Find
        # O(n^2 * log(n)), where n is the number of points

        n = len(points)
        edges = []

        # Generate all edges with their costs
        for i in range(n):
            for j in range(i + 1, n):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((distance, i, j))

        # Sort edges by distance (first element in tuple)
        # Python uses "Timsort", which is O(n * log(n))
        edges.sort()

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            # rank sorted union
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1
                return True # united successfully
            return False # already united, will cause a cycle

        total_cost = 0
        edges_used = 0

        for cost, node1, node2 in edges:
            if union(node1, node2):
                total_cost += cost
                edges_used += 1
                if edges_used == n - 1:
                    break

        return total_cost