fruits = ["Apple", "Orange", "Pear", "Strawberry", "Peach"]
vegetables = ["Cucumber", "Tomato", "Carrot", "Kale", "Cabbage"]

dirty_dozen = [fruits, vegetables]
dirty_dozen[0].append("Cherry")

print(dirty_dozen[0][1])

# So the dirty_dozen list have only 2 items which are inner lists. And we can access their elements like
# dirty_dozen[0(first inner list)][1(that`s the element of the 1st inner list)]
