numbers = []
even_numbers = []

while True:
    user_input = input("Enter an integer (or type 'QUIT' to stop): ")
    
    if user_input == "QUIT":
        break
    
    num = int(user_input)
    numbers.append(num)
    if num % 2 == 0:
        even_numbers.append(num)

print("\nAll numbers entered:", numbers)
print("Even numbers:", even_numbers)
