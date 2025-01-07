class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        # Game of Life, without extra memory
        # Cell states:
        # 0: dead -> dead
        # 1: alive -> alive
        # 2: dead -> alive
        # 3: alive -> dead
        # O(m * n), since we need to process each and every cell

        m = len(board)
        n = len(board[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        def count_alive_neighbors(cell_row, cell_col):
            alive_count = 0

            for direction_row, direction_col in directions:
                new_row = cell_row + direction_row
                new_col = cell_col + direction_col

                if 0 <= new_row < m and 0 <= new_col < n: # if the cell is within the board
                    if board[new_row][new_col] == 1 or board[new_row][new_col] == 3: # if the cell is alive
                        alive_count += 1
            return alive_count

        # Apply rules for each cell
        for r in range(m):
            for c in range(n):
                alive_neighbors = count_alive_neighbors(r, c)

                # Rules
                if board[r][c] == 1: # If alive
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        board[r][c] = 3  # will die
                elif board[r][c] == 0:  # If dead
                    if alive_neighbors == 3:
                        board[r][c] = 2  # Will become alive

        # Apply changes
        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:
                    board[r][c] = 1
                elif board[r][c] == 3:
                    board[r][c] = 0