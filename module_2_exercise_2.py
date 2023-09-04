input = input("Enter a string: ")
lowercase = ""
uppercase = ""
for char in input:
    if char.islower():
        lowercase += char
    elif char.isupper():
        uppercase += char
input = input.replace(" ", "")
result = lowercase + uppercase
print(result)
