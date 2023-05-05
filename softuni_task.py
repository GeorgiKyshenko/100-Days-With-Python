x = int(input())
y = int(input())
z = int(input())

for i in range(1, x + 1):
    if i % 2 == 0:
        for j in range(2, y + 1):
            if j == 9:
                continue
            elif j == 2 or j % 2 != 0:
                for k in range(1, z + 1):
                    if k % 2 == 0:
                        print(f'{i} {j} {k}')
