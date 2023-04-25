row1 = ["  ", "  ", "  "]
row2 = ["  ", "  ", "  "]
row3 = ["  ", "  ", "  "]

treasure_map = [row1, row2, row3]
emoji = "🐶"

while True:
    position = (input("Type the coordinates:"))
    horizontal = int(position[0]) - 1
    vertical = int(position[1]) - 1
    if treasure_map[horizontal][vertical] != emoji:
        treasure_map[horizontal][vertical] = emoji
    else:
        print("All positions are occupied. The Game is Over!")
        break
    print(f"{row1}\n{row2}\n{row3}")
