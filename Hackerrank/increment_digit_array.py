
# Taken as a whole, such an array represents a positive integer number. 
# The rightmost position of the array represents the least siginificant digit of the number.

# An example digit array is [4, 2] which represents the integer 42.

# In this challenge, you will write a function to increment the number in the digit array by 1. 
# For example, upArray([4, 2]) will return the array [4, 3].

# Examples
# arr -	Return Value
# [5,7,4] - [5,7,5]
# [4,3,9] - [4,4,0]

from typing import List
def up_array(numbers: List[int]) -> List[int]:
    if not numbers:
        return []
    if len(numbers) == 1 and numbers[0] == 9:
        return [1,0]
    numbers[-1] += 1
    for i in range(len(numbers) - 1, 0, -1):
        if numbers[i] == 10:
            numbers[i] = 0
            numbers[i-1] += 1
    if numbers[0] == 10:
        numbers[0] = 0
        numbers.insert(0, 1)
    return numbers  

print(up_array([4, 2, 5]))