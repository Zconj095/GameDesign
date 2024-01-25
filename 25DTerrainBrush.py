'''The function body is made up of four statements. The first statement assigns the values of the brush_position argument to a variable x and y. The second statement uses a for loop to iterate over a range of indices that includes the y indices within the specified brush_size of the brush_position argument. The third statement uses another for loop to iterate over a range of indices that includes the x indices within the specified brush_size of the brush_position argument.

Within each iteration of the inner for loop, the function checks if the current index is within the bounds of the terrain_grid argument using two if statements. If the index is within the bounds, the function updates the value at the current index in the terrain_grid argument by adding the height_change argument to the existing value.

The final two statements in the function body are examples of how the function can be used. The first statement creates a 10x10 2D list terrain and initializes each element to 0. The second statement calls the apply_terrain_brush() function with the terrain list as the first argument, the tuple (5, 5) as the second argument (which represents the brush_position argument), 2 as the third argument (which represents the brush_size argument), and 1 as the fourth argument (which represents the height_change argument).'''
def apply_terrain_brush(terrain_grid, brush_position, brush_size, height_change):
    """
    Apply a 2.5D terrain brush effect on a terrain grid.

    :param terrain_grid: The 2D grid representing the terrain
    :param brush_position: (x, y) position of the brush on the grid
    :param brush_size: Size of the brush
    :param height_change: The change in height to apply
    """
    x, y = brush_position
    for i in range(y - brush_size, y + brush_size + 1):
        for j in range(x - brush_size, x + brush_size + 1):
            if 0 <= i < len(terrain_grid) and 0 <= j < len(terrain_grid[0]):
                terrain_grid[i][j] += height_change

# Example Usage
terrain = [[0 for _ in range(10)] for _ in range(10)]  # 10x10 terrain grid
apply_terrain_brush(terrain, (5, 5), 2, 1)  # Apply brush at position (5,5) with size 2 and height change 1