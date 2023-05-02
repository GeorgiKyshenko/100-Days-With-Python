def separator():
    print("-----------------------------")


dictionary = {
    1: "Apple",
    "string": "Orange",
    "string2": "Orange",
    3: "Peach"
}

# Getting element from the dictionary
print("1.Getting element from the dictionary")
print(dictionary[1] + ", " + dictionary["string"])
# or
print(dictionary.get(1) + ", " + dictionary.get("string"))
separator()

# Adding elements with non-existent Key. If we use a Key value that is already in the dictionary, it overwrites it
print("2.Adding elements with non-existent Key.")
dictionary[4] = "Cherry"
print(dictionary)
separator()

# Edit the value of an existing key.
print("3.Edit the value of an existing Key.")
dictionary[1] = "Green Apple(Edited)"
print(dictionary)
separator()

# Print dictionary elements
print("4.Print dictionary elements")
print(dictionary)
separator()

# Loop in dictionary
print("5.Loop in dictionary")
for key in dictionary:
    print(f"{key} - {dictionary[key]}", end=", ")
print()
separator()

# Wipe out a dictionary
print("6.Wipe out a dictionary")
dictionary = {}
print(f"{dictionary}")


