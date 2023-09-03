n = int(input("Enter an integer greater than 1: "))
if n <= 1:
    print("Please enter an integer greater than 1.")
else:
    for i in range(n + 1):
        print(f"The cube of {i} is {i**3}")
