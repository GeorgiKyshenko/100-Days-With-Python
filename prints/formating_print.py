# in Python, we can NOT concatenate int values with string. We have to either cast them to string or use f""
text_length = len(input("Write a text:\n"))
str_value = str(text_length)
print("Your text length is: " + str_value)

text2_length = len(input("Write a new text:\n"))
print(f"Your new text length is: {text2_length}")
