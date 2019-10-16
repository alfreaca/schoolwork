grid = [["x"] * 4] * 6
print(grid)

coord_x = 0
coord_y = 0


oldcoord_x = coord_x
oldcoord_y = coord_y

grid[oldcoord_x-1][oldcoord_y-1] = "x"

coord_x = int(input("Input the x co ordinate: "))
coord_y = int(input("Input the y co ordinate: "))

# grid[1][1] = "O"

print(grid)



