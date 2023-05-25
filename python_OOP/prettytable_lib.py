from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Animal Type", ["Tiger", "Dolphin", "Dog"])
table.add_column("Habitat", ["Land", "Sea", "Land"])
table.align = "l"
print(table)
