class Solution(object):
    def numIslands(self, grid):
        def flood_island(rowIndex, colIndex): # method will flood the island to prevent revisiting
            # if out of bound or water encountered - do nothing
            if (rowIndex < 0
                    or colIndex < 0
                    or rowIndex >= rows
                    or colIndex >= cols
                    or grid[rowIndex][colIndex] == '0'):
                return

            # mark the cell as visited by flooding it
            grid[rowIndex][colIndex] = '0'

            # flood the island in all directions
            flood_island(rowIndex + 1, colIndex)
            flood_island(rowIndex - 1, colIndex)
            flood_island(rowIndex, colIndex - 1)
            flood_island(rowIndex, colIndex + 1)

        rows = len(grid)
        cols = len(grid[0])
        island_count = 0

        for rowIndex in range(rows):
            for colIndex in range(cols):
                if grid[rowIndex][colIndex] == '1':
                    island_count += 1
                    flood_island(rowIndex, colIndex)

        return island_count
