grid = [["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"], 
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]]
# Create a function that takes a grid of # and -, where each hash (#) represents a mine and each dash (-) represents a mine-free spot.
def grid_to_string(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "-":
                count = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[i]) and grid[i + x][j + y] == "#":
                            count += 1
                grid[i][j] = str(count)
    return grid

print(grid_to_string(grid))
    