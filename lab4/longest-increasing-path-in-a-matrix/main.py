class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # DFS with memoization
        # O(m * n), where m = rows, n = columns
        m, n = len(matrix), len(matrix[0])

        longest = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            # cache hit
            if longest[i][j] != -1:
                return longest[i][j]

            max_length = 1 # current cell is 1-length already
            if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                max_length = max(max_length, 1 + dfs(i - 1, j))  # Up
            if i + 1 < m and matrix[i + 1][j] > matrix[i][j]:
                max_length = max(max_length, 1 + dfs(i + 1, j))  # Down
            if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                max_length = max(max_length, 1 + dfs(i, j - 1))  # Left
            if j + 1 < n and matrix[i][j + 1] > matrix[i][j]:
                max_length = max(max_length, 1 + dfs(i, j + 1))  # Right

            longest[i][j] = max_length
            return longest[i][j]

        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))

        return result