# Create the rows
row1 = ['😊', '😊', '😊']
row2 = ['😊', '😊', '😊']
row3 = ['😊', '😊', '😊']

# Create the nested list
matrix = [row1, row2, row3]

# Print initial matrix
print(f"{row1}\n{row2}\n{row3}")

# Take user input
position = input("Enter the position where you want to hide your money: ")

# Extract row and column, convert to int, and adjust for 0-indexing
row_num = int(position[0]) - 1
col_num = int(position[1]) - 1

# Update the matrix
matrix[row_num][col_num] = 'x'

# Print the final matrix
print(f"{row1}\n{row2}\n{row3}")