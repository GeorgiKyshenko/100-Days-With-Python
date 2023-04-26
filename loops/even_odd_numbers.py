import random

print(f"All the odd numbers to 100 are: ")
for i in range(1, 101, 2):
    if i < 99:
        print(i, end=", ")
    else:
        print(i)


print(f"All the even numbers to 100 are: ")
for i in range(0, 101, 2):
    if i < 100:
        print(i, end=", ")
    else:
        print(i)
