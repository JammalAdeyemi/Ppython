# Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.

### Thought Process and Concepts Utilized
# 1. Problem Understanding:
# - The task is to determine if an integer `x` is a palindrome without converting it to a string. A palindrome number
# reads the same backward as forward.
# - Key considerations include handling negative numbers and efficiently comparing digits without string conversion.
# - The challenge is to devise a method to reverse part of the number and compare it with the other part directly in
# numerical form.

# 2. Algorithm Choice:
#- Reversing Half the Number: To avoid converting the integer into a string, the algorithm reverses the second half 
# of the number and compares it with the first half. If both halves are equal, the number is a palindrome.
#- Iterative Approach: An iterative method is chosen to extract and reverse the digits of the second half of the 
# number while reducing the first half accordingly. This approach is efficient and works within the constraints of 
# not using extra space for string conversion.
#- Handling Edge Cases: Special care is taken to handle cases like negative numbers and numbers ending in zero, as 
# these are not palindromes by definition (except for 0 itself).

# 3. Implementation Details:
#- Initial Checks: Check if `x` is negative or ends with 0 (and is not 0 itself); in these cases, return `False` 
# immediately.
#- Reversing Half of the Number: Iteratively build the reversed second half of the number. In each iteration, add the
# last digit of `x` to `reversed_half` and remove the last digit from `x`. Continue this process until `reversed_half`
# is greater than or equal to `x`.
#- Comparison: Compare `x` (the reduced first half) with `reversed_half`. For even digits, they should be equal. For
# an odd number of digits, ignore the middle digit in `reversed_half` by comparing `x` with `reversed_half // 10`.

class Solution(object):
    def isPalindrome(self, x):
        """
        Check if an integer is a palindrome without converting it to a string.
        :type x: int
        :rtype: bool
        """
        # Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For odd number of digits, we can get rid of the middle digit by reversed_half//10
        return x == reversed_half or x == reversed_half // 10

# Explanation
# • Handling Special Cases: Negative numbers and numbers ending in 0 (except 0 itself) cannot be palindromes.
# • Reversing Half of the Number: We continuously take the last digit of x and add it to reversed_half, which is 
# constructed in reverse order. We stop this process when reversed_half becomes equal to or greater than x.
# • Comparison: We compare the first half of the number (x) with the reversed second half (reversed_half). For numbers 
# with an odd number of digits, the middle digit is in reversed_half, so we compare x with reversed_half // 10.

# Time & Space Complexities
# • Time Complexity: O(log n), where n is the value of the integer. The complexity is due to the division process, 
# which essentially halves the number at each step.
# • Space Complexity: O(1), as the space used is constant and does not depend on the size of the input number. Only
# a few variables are used for the calculations.