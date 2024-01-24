grayscale_image = [[236, 189, 189, 0],
                   [236, 80, 189, 189],
                   [236, 0, 189, 80],
                   [236, 189, 189, 80]]
# We can access the elements of the list using the following syntax
print("Example 1")
print(grayscale_image[0][0])
print(grayscale_image[0][1])
print(grayscale_image[0][2])
print(grayscale_image[0][3])
print()

# we intialise variables for the specific size of the grid.
# In this case we have a 3 by 2 grid.
number_of_rows = 3
number_of_columns = 2
# We create the None value twice in a list for the columns, and we employ a loop to do it three times for the number of rows.
empty_grid = [[None] * number_of_columns for _ in range(number_of_rows)]
print("Example 2")
print(empty_grid)
print()

# ASSIGNING VALUES TO ELEMENTS IN A TWO-DIMENSIONAL LIST
last_pixel = grayscale_image[3][3]
print("Example 3")
print(last_pixel)
print()
print("Example 4")

student_scores = [ [72, 85, 87, 90, 69],
[80, 87, 65, 89, 85],
[96, 91, 70, 78, 97],
[90, 93, 91, 90, 94] ]
# Use a for loop to print the entire elements of the two dimensional array.
row_index = 0
for row in student_scores: # outer loop for rows
    print(f'Term {row_index + 1}: ') #row index used for the term number
    row_index +=1 #increment row index
    for col in row: # inner loop for columns
        print(col, end = "% ") # print each column value with percentage symbol
    print()

#  NON-RECTANGULAR LISTS
print()
print("Example 5")
ragged_list = [ [ 1, 2, 3 ] ,
                [ 4, 5 ], 
                [ 6 ], 
                [ 7, 8, 9, 10 ] ]
rows = len(ragged_list)
for row in range(rows):
    cols = len(ragged_list[row]) # now the number of cols depends on each row’s length
    print("Row", row, "has", cols, "columns: ", end="")
    for col in range(cols):
        print(ragged_list[row][col], " ", end="")
    print()

