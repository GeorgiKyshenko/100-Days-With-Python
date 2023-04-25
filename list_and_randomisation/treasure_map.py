def cell_check(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "  ":
                return True
    return False


row1 = ["  ", "  ", "  "]
row2 = ["  ", "  ", "  "]
row3 = ["  ", "  ", "  "]

treasure_map = [row1, row2, row3]
emoji = "🐶"
is_the_map_empty = True

while is_the_map_empty:
    position = (input("Type the coordinates:"))
    horizontal = int(position[0]) - 1
    vertical = int(position[1]) - 1
    if treasure_map[horizontal][vertical] != emoji:
        treasure_map[horizontal][vertical] = emoji
    else:
        if cell_check(treasure_map):
            print("The position is already occupied. Choose another!")
            continue
        else:
            is_the_map_empty = False
            continue
    print(f"{row1}\n{row2}\n{row3}")
print("All cells are occupied. Game is Over!")
