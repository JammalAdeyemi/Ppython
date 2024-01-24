# A quality agent is responsible for inspecting samples of the finished products in the production line. 
# Each sample contains defective and non-defective products represented by 1 and 0 respectively.  
# The product samples are placed sequentially in a two dimensional square matrix. 
# The goal is to determine the size of the largest square of defective products in the two dimensional square matrix.

# Complete the 'findLargestSquareSize' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY samples as parameter.
#

def findLargestSquareSize(samples):
    # Write your code here
    n = len(samples)
    m = len(samples[0])
    dp = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if samples[i][j] == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = 0
    for i in range(1, n):
        for j in range(1, m):
            if samples[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    return max([max(i) for i in dp])


# Explanation:
# The function then initializes two variables "n" and "m" to be the length of the rows and columns of the input array respectively. 
# The function then creates a 2D array "dp" with the same dimensions as the input array, and initializes all the elements of this array to be 0.

# The function then iterates through all the elements of the input array and checks if the element is equal to 1, 
# if so the corresponding element of the dp array is set to 1 else it is set to 0.

# Then the function iterates through the dp array starting from the second row and second column, and for each element if it is equal to 1, 
# it updates its value to be the minimum of the value of the element above it, to the left of it and the element diagonally above 
# and to the left of it, plus 1.

# Finally, the function returns the maximum value in the dp array which corresponds to the size of the largest square 
# sub-matrix consisting of only 1s in the input array.