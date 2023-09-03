user_input = input("Enter a string: ")

c_list = list(user_input)

sublist = [c_list[i:i+3] for i in range(0, len(c_list), 3)]

print("\nList of characters:", c_list)
print("List of sublists:", sublist)
