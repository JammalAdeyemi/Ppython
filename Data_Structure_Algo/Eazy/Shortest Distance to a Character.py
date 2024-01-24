# Shortest Distance to a Character
# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.
# The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

### Thought Process and Concepts Utilized
# 1.Problem Understanding:
# -The task is to find the shortest distance from each character in a given string `s` to a specified 
# character `c`. The distance is measured in terms of the number of characters between positions.
# -A key part of the problem is understanding that the closest occurrence of `c` to any character in `s`
# could be either to its left or right. 
# -The challenge lies in efficiently calculating these distances for each character in the string without 
# redundant calculations.

# 2.Algorithm Choice:
# -Two-Pass Linear Scan: A two-pass approach is chosen for its efficiency and simplicity. The idea is to 
# make one pass from left to right to find the distance to the nearest occurrence of `c` on the left side, 
# and another pass from right to left to do the same for the right side.
# -Minimization Strategy: After both passes, the minimum distance obtained from either side for each 
# character gives the shortest distance to `c`. This method ensures that we consider the closest occurrence 
# of `c` in either direction.
# -Initial Large Values: Initializing the result array with large values (e.g., length of the string) as 
# placeholders. This is important because it provides a starting point to compare and find the min 
# distance during each pass.
# -Efficient Distance Calculation: The use of the absolute difference in indices to calculate the distance
# is straightforward and avoids unnecessary complexity. The update of the `pos` variable (which tracks the
# most recent occurrence of `c`) during each iteration simplifies the distance calculation.


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        """
        Find the shortest distance to a character c in a string s.
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n = len(s)
        result = [n] * n  # Initialize with a large number
        pos = -n  # Position of the most recent occurrence of c

        # First pass: left to right
        for i in range(n):
            if s[i] == c:
                pos = i
            result[i] = min(result[i], abs(i - pos))

        # Second pass: right to left
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                pos = i
            result[i] = min(result[i], abs(i - pos))

        return result

### Explanation
# -Initialization: Create an array `result` with the same length as `s` and initialize all elements to a 
# large number (the length of `s` is a safe upper bound).
# -First Pass (Left to Right): Iterate over `s` and update `pos` each time `c` is found. For each 
# character in `s`, calculate the distance to the nearest `c` on the left.
# -Second Pass (Right to Left): Iterate over `s` in the reverse direction and again update `pos` each 
# time `c` is found. Update the distance in `result` to the minimum of the current value and the distance 
# to the nearest `c` on the right.
# -Result: After both passes, `result` contains the shortest distance to `c` for each character in `s`.

### Time & Space Complexities
# -Time Complexity: O(n), where `n` is the length of the string `s`. Each character is visited twice in 
# separate linear passes.
# -Space Complexity: O(n) for the `result` array. No additional space that scales with the input size is 
# used beyond this array.