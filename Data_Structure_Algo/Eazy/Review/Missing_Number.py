# Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is
# missing from the array.

### Thought Process and Concepts Utilized
# 1. Problem Understanding:
#- The challenge is to identify the one missing number in an array that contains `n` distinct numbers ranging from 0
# to `n`.
#- It's understood that all numbers are present except for one, and the task is to find this missing number in an 
# efficient way.
#- The problem statement suggests a need for a solution that doesn't involve sorting or using additional data 
# structures, adhering to linear time complexity and constant space requirements.

# 2. Algorithm Choice:
#- Bitwise XOR Operation: This choice is motivated by the XOR operation's unique properties, where a number XORed 
# with itself yields 0, and a number XORed with 0 results in the original number. This property can be utilized to 
# isolate the missing number.
#- XORing Indices and Values: By XORing all indices and their corresponding values in the array, along with the 
# length of the array, the missing number can be found since all present numbers and their indices will cancel each
# other out.

# 3. Implementation Details:
#- Initial Missing Number: Initialize the `missing` variable with the length of the array (`n`), as it's the extra 
# number not covered in the array indices.
#- Iterative XOR Application: Iterate over the array using an index `i` and XOR `missing` with both the index and 
# the value at that index (`nums[i]`). The missing number will not be XORed and thus will remain in the `missing` 
# variable.
#- Final Result: The final value of `missing` after the loop is the missing number, as all other numbers and their 
# corresponding indices would have canceled themselves out through XOR operations.

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = len(nums)  # Start with n, as it's not included in the loop
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

## Explanation
#- Initial Missing Number: Initialize missing to n (the length of the array), as the numbers in nums are in the 
# range [0, n-1].
#- Iterative XOR Application: Iterate through the array, XORing each index i and its corresponding value num with 
# missing.
#- Finding the Missing Number: Since each number and its index will cancel each other out except for the missing 
# number, missing will hold the value of the missing number after completing the iteration.

## Time & Space Complexities
#- Time Complexity: O(n), where n is the number of elements in nums. The solution requires a single pass through the
# array.
#- Space Complexity: O(1), since the space used is independent of the input size. The algorithm only requires a 
# single variable to store the cumulative XOR result, aligning with the constant space requirement.

    