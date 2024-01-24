## Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

### Thought Process and Concepts Utilized
# 1. Problem Understanding:
# • The task is to find a contiguous subarray within an array `nums` that has the largest sum.
# • It's important to note that the subarray can start and end at any index within the array and must contain at 
# least one element.
# • The challenge lies in finding the most efficient way to traverse the array and keep track of the maximum sum 
# without having to consider every possible subarray explicitly.

# 2. Algorithm Choice:
# • Kadane's Algorithm: This is a well-known algorithm for solving the maximum subarray problem. It is chosen for 
# its efficiency in solving this problem with a single pass through the array.
# • Dynamic Programming Approach: Kadane's Algorithm uses principles of dynamic programming. It keeps track of the 
# maximum subarray sum ending at each position by considering the maximum of the current element and the sum of the current element with the maximum subarray sum ending at the previous position.

# 3. Implementation Details:
# • Initialization: Start with the first element of the array as both the current sum and the maximum sum.
# • Iterating Through the Array: Iterate from the second element to the end of the array.
    # - Update Current Sum: Calculate the current sum as the maximum of the current element itself and the sum of 
    # the current element with the current sum from the previous step. This step decides whether to extend the 
    # current subarray or start a new one from the current position.
    # - Update Max Sum: Continuously update the maximum sum if the current sum is greater than the maximum sum 
    # calculated so far.
# • Returning the Maximum Sum: After the iteration, the maximum sum variable holds the largest sum of any subarray.

class Solution(object):
    def maxSubArray(self, nums):
        """
        Find the subarray with the largest sum in an array.
        :type nums: List[int]
        :rtype: int
        """
        # Initialize variables to store the max sum so far and the current sum
        max_sum = current_sum = nums[0]
        # Iterate over the array starting from the second element
        for num in nums[1:]:
            # Update the current sum
            # If the current sum becomes negative, reset it to the current number
            current_sum = max(num, current_sum + num)
            # Update the max sum if the current sum is greater
            max_sum = max(max_sum, current_sum)
        return max_sum

### Explanation
# • Initialization: Start with the first element as the initial maximum and current sum.
# • Iterating Through the Array: For each element in the array (starting from the second element):
    # Update Current Sum**: The current sum is the maximum of the current element and the sum of the current 
    # element and the previous current sum. This step effectively decides whether to start a new subarray from the 
    # current element (if the previous sum was negative and less than the current element) or to continue with the 
    # current subarray.
    # Update Max Sum**: If the updated current sum is greater than the max sum, the max sum is updated. This ensures
    # we always have the maximum sum encountered so far.
# • Returning Result: The result is the maximum sum found during the iteration.

### Time & Space Complexities
# • Time Complexity: O(n), where `n` is the length of the array. The algorithm traverses the array once, performing 
# constant-time operations at each step.
# • Space Complexity: O(1), as the solution uses a constant amount of space regardless of the input size. Only a 
# few variables are needed to store the sums.

### Summary
# Kadane's Algorithm is an optimal solution for the maximum subarray problem due to its efficiency and simplicity. 
# The algorithm's clever use of dynamic programming principles allows it to find the maximum subarray sum with a 
# single pass through the array, avoiding the need for nested loops and thereby reducing the time complexity from 
# O(n²) to O(n). This approach is a classic example of using dynamic programming to break down a problem into 
# smaller, overlapping subproblems, solving each just once, and storing their solutions - all without needing 
# additional space proportional to the input size.