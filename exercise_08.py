numbers = []

for i in range(10):
    
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

unique_numbers = [num for num in numbers if numbers.count(num) == 1]

print("\nOriginal list:", numbers)
print("List with unique elements:", unique_numbers)
