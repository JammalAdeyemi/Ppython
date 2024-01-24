# 1. Array Reduction 2
# Given an array arr of n integers, in a single operation, one can choose two indices,/ and j, and delete arr[i] from the array if 
# 2* arr[i] < arr[j]. A particular element can be chosen at most once. Find the minimum possible size of the array after 
# performing the operation any number of times, possibly zero.
# Example
# Suppose n = 7 and arr= [1, 2, 3, 4, 16, 32, 64]
# • In the first operation, choose 1 and 16 and delete 1 from the array as 2* 1 ≤ 16. The array becomes [2, 3, 4, 16, 32, 64].
# • In the second operation, choose 2 and 32 and delete 2 from the array as 2* 2 ≤ 32. The array becomes [3, 4, 16, 32, 64].
# • In the third operation, choose 4 and 64 and delete 4 from the array as 2 * 4 ≤ 64. The array becomes [3, 16, 32, 64].
# Now the only element that has not been chosen is 3. There have. to be two elements, arr[i] and arr[j], for a comparison to 
# take place, so no more operations can occur. The minimum possible size of the array is 4. Note that there are multiple ways 
# to achieve 4 elements in the final array after performing the operations.
# Function Description
# Complete the function getMinSize in the editor below.
# getMinSize has the following parameter(s): arr[n]: an array of integers
# Returns
# int: the minimum possible size of the array
# Constraints
# • 1≤n≤2*105
# • 1 ≤ arr[i] ≤ 109

def getMinSize(arr):
    n = len(arr)
    arr.sort()  # sort the array in ascending order
    i, j = 0, 1  # initialize two pointers to the first two elements
    while j < n:
        if 2 * arr[i] < arr[j]:
            # if the condition is satisfied, remove the smaller element
            arr.pop(i)
            n -= 1
            j -= 1
        else:
            # otherwise, move the pointers to the next elements
            i += 1
            j += 1
    return n

# example usage:
arr = [1, 2, 3, 4, 16, 32, 64]
print(getMinSize(arr))  # output: 4


# 2. Find School Count
# Given the dataset of schools and the subjects they offer as a pandas dataframe, perform the following operations:
# Drop all the schools offering fewer than 3 subjects.
# • Clean the 'state_code' column such that it only contains alpha-numeric characters.
# • For each state, return the number of schools offering English, Maths, Physics and Chemistry, each in a separate column.
# The given dataframe consists of three columns:
# • school_id - School ID for each student
# • state_code - Unique identifier for each state
# • subjects - space-separated strings of subjects, all in lowercase
# Function Description
# Complete the function stateCount in the editor below.
# stateCount has the following parameter(s): df: a pandas dataframe
# Returns
# pandas dataframe: the results of processing maintaining the original order that state codes are encountered
# Constraints
# • 1 < number of rows in df < 1000

import pandas as pd
import re

def stateCount(df):
    # Drop all the schools offering fewer than 3 subjects.
    df = df[df['subjects'].str.count(' ') >= 2]

    # Clean the 'state_code' column such that it only contains alpha-numeric characters.
    df['state_code'] = df['state_code'].apply(lambda x: re.sub('[^0-9a-zA-Z]+', '', x))

    # Split the 'subjects' column into separate columns for each subject.
    df[['English', 'Maths', 'Physics', 'Chemistry']] = df['subjects'].str.split(' ', expand=True)

    # For each state, count the number of schools offering each subject.
    result = df.groupby('state_code').agg({'English': 'count', 'Maths': 'count', 'Physics': 'count', 'Chemistry': 'count'})

    # Combine the results into a new dataframe and return it.
    return result

# example usage:
df = pd.DataFrame({
    'school_id': [1, 2, 3, 4, 5],
    'state_code': ['CA', 'CA', 'NY', 'NY', 'NY'],
    'subjects': ['english maths physics', 'maths physics chemistry', 'english maths', 'physics chemistry', 'english maths physics chemistry']
})
print(stateCount(df))


b = [0,1,2,3,4,5,6,7,8,9]
print(b[::3])

print("John\nCharles\nChris")