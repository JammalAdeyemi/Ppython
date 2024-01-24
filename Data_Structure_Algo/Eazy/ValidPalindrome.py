## Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
# non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and 
# numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

## Thought Process and Concepts Utilized
# 1. Understanding the Problem: The task is to determine if a given string is a palindrome. A string is a palindrome 
# if it reads the same forward and backward. However, there's a twist: we need to consider only alphanumeric 
# characters (letters and numbers) and ignore casing.
# 2. Algorithm Choice:
# * String Manipulation: The core of this problem involves string manipulation - converting to lowercase and 
# filtering out non-alphanumeric characters.
# * Palindrome Check: After processing the string, the next step is to check if it reads the same forward and 
# backward. This can be achieved by comparing the processed string with its reverse.
# 3. Implementation Details:
# 1. Lowercase Conversion and Filtering: Use list comprehension to iterate over each character in s, convert it to 
# lowercase using char.lower(), and include it in the new list if char.isalnum() is True.
# 2. Palindrome Verification: Compare the list of filtered characters with its reverse 
# (filtered_chars == filtered_chars[::-1]). In Python, the slicing operation [::-1] efficiently reverses a list or 
# string.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Convert the string to lowercase and remove non-alphanumeric characters
        filtered_chars = [char.lower() for char in s if char.isalnum()]

        # Check if the filtered string is a palindrome
        return filtered_chars == filtered_chars[::-1]
        