row_number = int(input("Enter the row number (1-5): "))
column_number = int(input("Enter the column number (1-5): "))

if 1 <= row_number <= 5 and 1 <= column_number <= 5:
    grid = [[0] * 5 for _ in range(5)]
    grid[row_number - 1][column_number - 1] = 1

    print("Grid:")
    for row in grid:
        print(' '.join(map(str, row)))
else:
    print("Please enter valid row and column numbers between 1 and 5.")


