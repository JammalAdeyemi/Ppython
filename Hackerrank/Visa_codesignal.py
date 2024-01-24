# Given an array of integers numbers , find and return the index 1 of the first integer within the array 
# that is less than its adjacent integers on both sides. Note that to satisfy these criteria, adjacent 
# integers on both sides must exist.
# Return -1 if none of the integers in the given array fit the criteria.
# Assume that array indices are 0-based.
# Note: You are not expected to provide the most optimal solution, but a solution with time complexity not 
# worse than O (numbers. length?) will fit within theexecution time limit.

def solution(numbers):
    # Iterate over the array, skipping the first and last elements
    for i in range(1, len(numbers) - 1):
        # Check if the current element is less than its adjacent elements
        if numbers[i] < numbers[i-1] and numbers[i] < numbers[i+1]:
            # Return the index of the current element
            return i
    # If no element satisfies the criteria, return -1
    return -1

def solution(numbers):
    for i in range(1, len(numbers) - 1):
        if numbers[i - 1] > numbers[i] < numbers[i + 1]:
            return i
    return -1

# Given a 2-dimensional integer array named matrix, your task is to partition the matrix into 4 rectangular
# sub-matrices (each with at least one non-negative valued cell), while minimizing the difference between 
# the maximal and the minimal average values of the partitions. The average value of a partition is the 
# sum of all the non-negative values divided by the count of the non-negative values, rounded down.
# Return the row resRow and column resCol with the minimal difference between the
# maximal and the minimal average value of the partitions matrix [0..resRow] [0..resCol]
# matrix [O..resRow] [resCol+1..cols-1], matrix [resRow+1..rows-1][0..resColj, and
# matrix [resRow+1..rows-1] [resCol+1..cols-1]
# Expand to see a visual image of how row=r and column=c can partition the matrix of sizemxn into 4 rectangular sub-matrices.

def solution(matrix):
    rows, cols = len(matrix), len(matrix[0])
    # Initialize the result variables to -1
    resRow, resCol, minDiff = -1, -1, float('inf')
    # Iterate over all possible partition positions
    for r in range(1, rows - 2):
        for c in range(1, cols - 2):
            # Partition the matrix into 4 sub-matrices
            subMatrices = [
                matrix[0:r+1, 0:c+1], matrix[0:r+1, c+1:cols],
                matrix[r+1:rows, 0:c+1], matrix[r+1:rows, c+1:cols]
            ]
            # Compute the average value of each sub-matrix
            averages = [int(sub[sub >= 0].sum() / (sub >= 0).sum()) for sub in subMatrices]
            # Compute the difference between the maximal and minimal average values
            diff = max(averages) - min(averages)
            # Update the result variables if the current partition has a smaller difference
            if diff < minDiff:
                resRow, resCol, minDiff = r, c, diff
    # Return the row and column of the optimal partition
    return resRow, resCol

def solution(matrix):
    rows,cols = len(matrix), len(matrix[0])
    res_row, res_col, min_diff = 0, 0, float('inf')

    def partition(r, c):
        partitions = [
            (matrix[0:r + 1], matrix[r + 1:]),
            ([row[:c + 1] for row in matrix], [row[c + 1:] for row in matrix]),
        ]
        return partitions

    def average(part):
        non_negatives = [val for row in part for val in row if val >= 0]
        return sum(non_negatives) // len(non_negatives)

    for r in range(rows - 1):
        for c in range(cols - 1):
            partitions = partition(r, c)
            max_avg = max(average(part) for part in partitions)
            min_avg = min(average(part) for part in partitions)
            diff = max_avg - min_avg

            if diff < min_diff:
                min_diff = diff
                res_row, res_col = r, c

    return res_row, res_col


# Given an array of integers numbers and an array pattern representing a comparison pattern, find how many 
# subarrays of numbers match the given pattern. pattern can only contain the following integers:
# •pattern[i] = 1, represents that the number corresponding to this element of the pattern is greater than 
# the previous one.
# •pattern[i] = 0, represents that the number corresponding to this element of the pattern is equal to 
# the previous one.
# •pattern[i] = -1, represents that the number corresponding to this element of the pattern is less than the
# previous one.
# It is guaranteed that the 'numbers.length' > 'pattern. length'
def solution(numbers, pattern):
    count = 0
    for i in range(len(numbers)-len(pattern)):
        match = True
        for j in range(len(pattern)):
            if (pattern[j] == 1 and numbers[i+j] <= numbers[i+j+1]) or \
               (pattern[j] == 0 and numbers[i+j] != numbers[i+j+1]) or \
               (pattern[j] == -1 and numbers[i+j] >= numbers[i+j+1]):
                match = False
                break
        if match:
            count += 1
    return count

def solution(numbers, pattern):
    if not numbers or not pattern or len(pattern) == 0:
        return 0
    count = 0
    for i in range(len(numbers) - len(pattern) + 1):
        matched = True
        for j in range(1, len(pattern)):
            if pattern[j] == 1:
                if numbers[i + j] <= numbers[i + j - 1]:
                    matched = False
                    break
            elif pattern[j] == 0:
                if numbers[i + j] != numbers[i + j - 1]:
                    matched = False
                    break
            elif pattern[j] == -1:
                if numbers[i + j] >= numbers[i + j - 1]:
                    matched = False
                    break
        if matched:
            count += 1

    return count

# You are given an array of integers numbers. Your task is to count the number of distinct pairs (1, j) 
# such that 0 5 1 < 5 < numbers. length, numbers [1] and numbers (31 have the same number it digits, and 
# exactly one of the digits differs between numbers [i] and numbers [j]
# Example
# For numbers = [1, 151, 241, 1, 9, 22,351] , the output should be
# solution (numbers) = 3
# • numbers [0] = 1 differs from numbers [4] = 9 on the one and only digit in both numbers.
# • numbers [1] = 151 differs from numbers [6] = 351 on the first digit.
# • numbers [3] = 1 differs from numbers [4] = 9 on the one and only digit in both numbers.
# Note that numbers [01 = 1 and numbers [3] = 1 do not differ from each other at all and thus
def solution(numbers):
    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Check if only one digit differs
            if numbers[i] != numbers[j] and sum(a != b for a, b in zip(str(numbers[i]), str(numbers[j]))) == 1:
                count += 1
    return count
    

def solution(numbers):
    count = 0
    for i in range(1, len(numbers)):
        for j in range(i+1, len(numbers)):
            if len(str(numbers[i])) == len(str(numbers[j])):
                diff_count = 0
                for k in range(len(str(numbers[i]))):
                    if str(numbers[i])[k] != str(numbers[j])[k]:
                        diff_count += 1
                if diff_count == 1:
                    count += 1
    return count
