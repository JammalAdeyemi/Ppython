## Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero 
# elements. Note that you must do this in-place without making a copy of the array.

## Thought Process and Concepts Utilized
# 1. Problem Understanding:
# • The task is to move all zeros in an integer array to the end while keeping the non-zero elements' relative order
# intact.
# • The operation must be done in-place, meaning no additional array can be used for storage.
# • This is a common array manipulation problem that tests understanding of efficient array traversal and element 
# swapping.

# 2. Algorithm Choice:
# • Two-Pointer Technique: A two-pointer technique is chosen for its efficiency and ability to solve the problem in 
# a single pass. This approach uses two pointers — one to iterate through the array and another to track the position
# for placing the next non-zero element. It's a popular technique for in-place array manipulation.
# • In-Place Swapping: Instead of creating a new array, non-zero elements are moved to the front via swapping, 
# ensuring that the operation is in-place.

# 3. Implementation Details:
# • Initializing Non-Zero Index Pointer: Start with a pointer (non_zero_index) at the beginning of the array to mark
# the position for the next non-zero element.
# • Iterating and Swapping: As the array is traversed, each non-zero element is swapped with the element at the 
# non_zero_index. After each swap, the non_zero_index is incremented to point to the next position.
# • End Result: By the end of the traversal, all non-zero elements maintain their relative order in the front, and 
# all zeros are moved to the end.

# 4. Time & Space Complexities:
# • Time Complexity: O(n), where n is the number of elements in the array. Each element is looked at exactly once.
# • Space Complexity: O(1), as the rearrangement is done in-place using a fixed number of variables 
# (no additional data structures are involved).

class Solution(object):
    def moveZeroes(self, nums):
        """
        Move all 0's to the end of the array while maintaining the relative order of the non-zero elements.
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Pointer for the position of the next non-zero element
        non_zero_index = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If the current element is non-zero
            if nums[i] != 0:
                # Swap the current element with the element at non_zero_index
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                # Increment the non_zero_index
                non_zero_index += 1
        # The function doesn't need to return anything as the modifications are made in-place
        
## Explanation
# • Non-Zero Index Pointer: Initialize a pointer non_zero_index to keep track of where the next non-zero element 
# should be placed. It starts at 0.
# • Iterating through the Array: Loop through each element in the nums array.
    # • If the current element is non-zero, swap it with the element at non_zero_index. This ensures that all 
    # non-zero elements are moved to the front of the array in their original order.
    # • Increment the non_zero_index.
# • In-Place Modification: Since the array is being modified in-place, there's no need to return anything from the
# function.
    