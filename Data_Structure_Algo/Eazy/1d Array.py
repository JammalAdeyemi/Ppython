# Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.

### Thought Process and Concepts Utilized
# 1. Problem Understanding:
#- The goal is to compute the running sum of an array, where each element in the resulting array represents the sum 
# of all elements up to that index in the original array.
#- The task requires an understanding of cumulative addition where each subsequent value depends on the sum of all 
# previous values in the array.
#- The challenge is to perform this operation efficiently, both in terms of time and space complexity.

# 2. Algorithm Choice:
# - In-Place Iterative Summation: Opting for an in-place update of the array to calculate the running sum. This 
# method is chosen for its simplicity and efficiency as it requires only a single pass through the array and does 
# not need additional space.
# - Linear Progression: The nature of the running sum calculation—each element's sum depends on the sum of elements
# before it—makes a linear, sequential approach appropriate.

# 3. Implementation Details:
# - Single Loop: Start iterating from the second element of the array (index 1), as the first element's running sum 
# is the element itself.
# - Cumulative Addition: For each element at index `i`, update its value to be the sum of its original value and the
# value at index `i-1`. This update reflects the running sum up to the current index.
# - In-Place Update: The array is updated in place, meaning no additional arrays are used to store the running sums.
# - Returning the Result: The original array, now modified to contain the running sums, is returned as the final 
# result.

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Iterate through the array, starting from the second element
        for i in range(1, len(nums)):
            # Add the previous sum to the current element
            nums[i] += nums[i - 1]
        return nums

## Explanation
#- Iterative Summation: Start iterating from the second element of the array (index 1). For each element at index i,
# update nums[i] by adding the value of the previous element (nums[i - 1]). This effectively accumulates the sum of 
# all elements up to the current index.
#– In-Place Update: The array nums is updated in place, thus avoiding the need for extra space for storing the 
# running sums.
#– Returning Result: Return the modified nums array, which now contains the running sum at each index.

## Time & Space Complexities
#– Time Complexity: O(n), where n is the number of elements in nums. Each element is visited once in the loop.
#- Space Complexity: O(1), as the computation is done in place, and no additional space is used that scales with the
# input size.
        