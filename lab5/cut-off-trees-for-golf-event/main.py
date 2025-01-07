class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # BFS
        # BFS: O(k * m * n), where k is the number of trees
        # Sort trees by height: O(k * log(k)), where k is the number of trees (using default sort)
        # Total: O(k * m * n + k * log(k))

        m = len(forest)
        n = len(forest[0])

        # Trees list with height and coordinates
        trees = []
        for row_index in range(m):
            for col_index in range(n):
                if forest[row_index][col_index] > 1:
                    height = forest[row_index][col_index]
                    trees.append((height, row_index, col_index))

        # Sort trees by height
        trees.sort()

        # Directions to neighbours for BFS
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # BFS for searching the shortest path between two trees
        def bfs(start, target):
            sr, sc = start # source row, source col
            tr, tc = target # target row, target col

            # Queue for processing cells
            queue = deque([(sr, sc, 0)])  # (row, col, steps)
            # Set for visited cells
            visited = {sr, sc}

            while queue:
                r, c, steps = queue.popleft()

                # If we reached the target
                if (r, c) == (tr, tc):
                    return steps

                # Check neighbours
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc # new row, new col

                    if 0 <= nr < m and 0 <= nc < n:
                        if (nr, nc) not in visited and forest[nr][nc] >= 1:
                            # If cell is not visited and is walkable
                            # Add to visited and processing queue
                            visited.add((nr, nc))
                            queue.append((nr, nc, steps + 1))
            # Unreachable
            return -1

        total_steps = 0
        start = (0, 0)

        for _, tr, tc in trees:
            steps = bfs(start, (tr, tc))
            if steps == -1:
                return -1
            total_steps += steps
            # Update current position
            start = (tr, tc)

        return total_steps