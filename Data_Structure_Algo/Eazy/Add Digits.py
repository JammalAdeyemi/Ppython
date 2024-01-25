# Add Digits
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

class Solution:
    def addDigits(self, num):
        while num > 9:
            num = sum([int(i) for i in str(num)])
        return num

### Code Explanation
# -The `while` loop continues as long as `num` has more than one digit, i.e., greater than 9.
# -Inside the loop, `num` is converted to a string (`str(num)`), which allows iteration over each digit 
# character.
# -A list comprehension (`[int(i) for i in str(num)]`) is used to convert each digit character back into 
# an integer and create a list of these integers.
# -The built-in `sum` function computes the sum of the integers in the list.
# -`num` is updated to this sum, and the loop repeats if `num` is still greater than 9.
# -Once `num` is reduced to a single digit, the loop exits, and `num` is returned.

### Time & Space Complexity
# -Time Complexity: O(N), where N is the number of iterations needed to reduce `num` to a single digit. 
# Each iteration involves converting the number to a string, iterating over its characters, and summing 
# them, which are all linear-time operations in the number of digits.
# -Space Complexity: O(M), where M is the number of digits in `num` at each iteration. This space is used 
# to store the list of digit integers generated by the list comprehension. As `num` decreases, M decreases,
# but in terms of space complexity analysis, we consider the worst case, which occurs during the first 
# iteration.