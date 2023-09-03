
float_number = int(input("Enter the number of floats: "))
if float_number <= 0:
    print("Please enter a positive integer.")
else:
    float_list = []
    for i in range(float_number):
        num = float(input(f"Enter float {i+1}: "))
        float_list.append(num)

    mean = sum(float_list) / float_number

    print("Entered list:", float_list)
    print("Mean:", mean)


