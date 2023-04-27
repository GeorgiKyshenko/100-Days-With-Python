def print_number(a, b, c):
    print(a, b, c)


# we can define in argument brackets which param is equal to what? It is called Keyword Argument
print_number(c=3, a=1, b=2)
# in this case it will assign the arguments in the order we inject them
print_number(3, 1, 2)


