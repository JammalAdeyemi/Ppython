## Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned 
# integer should be non-negative as well. You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

## Thought Process and Concepts Utilized
# 1. Problem Understanding: The goal is to find the square root of a non-negative integer, x, and round it down to the nearest integer.
# 2. Algorithm Choice: The binary search algorithm is ideal for this problem because it efficiently narrows down the search space. The square root of x will always be between 0 and x, and this range can be divided into two in each iteration to quickly find the answer.

## Implementation Details:
# 1. Initialize two variables, low (0) and high (x).
# 2. Continuously divide the range, checking if the middle value squared is equal to, less than, or greater than x.
# 3. Adjust low and high based on the comparison until low exceeds high.

## Edge Cases: Since the square root of 0 and 1 is themselves, these can be handled as special cases.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Special case handling for 0 and 1, as their square roots are themselves
        if x < 2:
            return x

        # Initialize the low and high pointers for binary search
        low, high = 1, x

        # Perform binary search
        while low <= high:
            # Find the mid-point of the current range
            mid = (low + high) // 2

            # Check if the square of mid is equal to, less than, or greater than x
            if mid * mid == x:
                return mid  # Mid is the exact square root
            elif mid * mid < x:
                low = mid + 1  # Adjust the lower bound
            else:
                high = mid - 1  # Adjust the upper bound

        # When low exceeds high, high is the integer part of the square root of x
        return high
        