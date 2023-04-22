print("Welcome to print calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give ? 10, 12 or 15? "))
tips = (10, 12, 15)

while tip_percentage not in tips:
    print("You should choose one of the following:")
    tip_percentage = int(input("What percentage tip would you like to give ? 10, 12 or 15? "))

persons = int(input("How many people to split the bill? "))
tip_as_percent = tip_percentage / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / persons
print(f"Each person should pay: {bill_per_person:.2f}$")

# OR
# final_amount = "{:.2f}".format(bill_per_person)
# print(f"Each person should pay: {final_amount}$")
