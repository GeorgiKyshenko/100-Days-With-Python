import random

names = input("Enter the names:").split(", ")
person_index = random.randint(0, len(names) - 1)
print(f"{names[person_index]} is going to pay the bill!")

# we can use another strategy

person_who_will_pay = random.choice(names)
print(person_who_will_pay)
