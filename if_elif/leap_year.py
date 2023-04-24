year = int(input())
leap_year = True

if year % 4 == 0:
    pass
    if year % 100 == 0:
        leap_year = False
        if year % 400 == 0:
            leap_year = True

if leap_year:
    print(f"The year {year} is a leap year!")
else:
    print(f"The year {year} is not a leap year")
