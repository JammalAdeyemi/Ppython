# Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. 
# You must implement a solution with a linear runtime complexity and use only constant extra space.

### Thought Process and Concepts Utilized
# 1. Problem Understanding:
#- The problem is to identify the unique number in an array where every other number appears exactly twice.
#- The constraints emphasize linear time complexity and constant space usage, ruling out approaches like hash tables
# or sorting.
#- Recognizing the properties of bitwise operations, especially XOR, is key to solving this problem efficiently.

#2. Algorithm Choice:
#- Bitwise XOR: Chosen due to its unique properties which suit the problem perfectly. Specifically, a number XORed 
# with itself yields 0, and any number XORed with 0 results in the original number.
#- Linear Scan: This approach involves iterating through the array once and applying the XOR operation continuously,
# which aligns with the requirement of linear time complexity.

# 3. Implementation Details:
#- Initialize Accumulator: Start with an accumulator variable, `result`, set to 0. This will hold the cumulative XOR
# result.
#- Iterative XOR Application: Iterate through each number in the array. Apply the XOR operation between the 
# accumulator (`result`) and each number. Due to the XOR property, pairs of identical numbers will cancel each other
# out.
#- Extracting the Unique Number: After processing the entire array, the accumulator will hold the unique number, as 
# all pairs would have nullified each other.
#- Return Result: The final value in `result` after completing the iteration is the single number that does not 
# repeat in the array.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result

## Explanation
#- XOR Operation: Initialize a variable `result` to 0. Iterate through each number in the array `nums` and XOR it 
# with `result`.
#- Finding the Single Number: Since XORing a number with itself results in 0, and XORing any number with 0 results 
# in that number, all pairs of numbers in the array will cancel each other out, leaving only the single number.
#- Return Result: The final value of `result` after the loop is the single number that appears only once in the array.

## Time & Space Complexities
#- Time Complexity: O(n), where `n` is the number of elements in the array `nums`. The algorithm needs to iterate 
# through each element of the array once.
#- Space Complexity: O(1), as the space used does not depend on the size of the input array. The only additional storage 
# used is the `result` variable.
	  