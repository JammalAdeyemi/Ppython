## Thought Process and Concepts Utilized
# 1. Problem Understanding:
# - The problem involves calculating the perimeter of an island on a grid, where `1` represents land and `0` represents water.
# - The grid cells are only connected horizontally and vertically.
# - The perimeter is the count of the edges of land cells that either border water or the boundary of the grid.

# 2. Algorithm Choice:
# - Iterative Grid Traversal: The solution iterates over each cell in the grid, checking if it's a part of the island (land) and then calculating its contribution to the perimeter.
# - Count and Adjust Method: Instead of checking all four sides of a land cell, the approach adds 4 (the maximum possible contribution of a land cell to the perimeter) and then subtracts for the shared edges with other land cells.

# 3. Implementation Details:
# - Initial Perimeter Count: Start with a perimeter of 0. For each land cell encountered, initially add 4 to the perimeter.
# - Adjusting for Shared Edges: For each land cell, check the left and upper neighboring cells (to avoid double counting). If a neighbor is also land, subtract 2 from the perimeter (each shared edge with a neighbor reduces the perimeter by 2).
# - Grid Traversal: Use nested loops to iterate over each cell in the grid, applying the above logic to compute the perimeter.

# 4. Time & Space Complexities:
# - Time Complexity: O(N * M), where N is the number of rows and M is the number of columns in the grid. Each cell in the grid is visited exactly once.
# - Space Complexity: O(1), as the solution does not use any additional data structures that grow with the size of the input. The space used is for a few variables, which is constant.

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0 # Initialize perimeter
        # Iterate through each row
        for row in range(len(grid)):
            # Iterate through each column
            for col in range(len(grid[0])):
                # If the current cell is land
                if grid[row][col] == 1:
                    # Add 4 to the perimeter
                    perimeter += 4
                    # If the cell to the left is also land
                    if col > 0 and grid[row][col - 1] == 1:
                        # Subtract 2 from the perimeter
                        perimeter -= 2
                    # If the cell above is also land
                    if row > 0 and grid[row - 1][col] == 1:
                        # Subtract 2 from the perimeter
                        perimeter -= 2
        return perimeter # Return the perimeter
        