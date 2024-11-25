class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # as a default, each cell has 4 water sides
                    perimeter += 4

                    # if the cell has a neighbor,
                    # we will subtract 2 from the perimeter
                    # because each side are shared by two cells
                    # it is valid for left and top sides,
                    # because we are iterating left-right and top-bottom
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
        return perimeter