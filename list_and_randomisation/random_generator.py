import random
import importing_file

# range from 1 to 100 (we can set whatever range)
random_integer = random.randint(1, 100)
print(random_integer)

# generate random float number. If we don't multiply it generates random float between 0-1 but one exclusively (0.99999)
random_float = random.random() * 5
print(random_float)

# getting variables of imported files and sum them
sum_of_variables = importing_file.a + importing_file.b
print(sum_of_variables)
