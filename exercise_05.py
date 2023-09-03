list1 = []
list2 = []

print("Enter values for the first list:")
for i in range(5):
    num = int(input(f"Enter integer {i+1}: "))
    list1.append(num)

print("Enter values for the second list:")
for i in range(5):
    num = int(input(f"Enter integer {i+1}: "))
    list2.append(num)

common_elements = list(set(list1) & set(list2))
print("\nFirst list:", list1)
print("Second list:", list2)
print("Common elements:", common_elements)


