number = int(input())
flag = False
count = 0
for a in range(1, 9 + 1):
    for b in range(9, a, -1):
        for c in range(0, 9 + 1):
            for d in range(9, c, -1):
                sums = a + b + c + d
                multiply = a * b * c * d
                if sums == multiply and number % 10 == 5:
                    count += 1
                    print(f"{a}{b}{c}{d}")
                    flag = True
                    break
                elif multiply // sums == 3 and number % 3 == 0:
                    count += 1
                    print(f"{d}{c}{b}{a}")
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        break
if count == 0:
    print("Nothing found")
