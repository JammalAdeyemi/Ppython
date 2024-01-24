## First Unique Character in a String
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, 
# return -1.

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## 1. Brute Force: O(n^2) time and O(1) space
        # Iterate through the string
        for i in range(len(s)):
            # Check if the current character is unique
            if s.count(s[i]) == 1:
                # Return the index of the unique character
                return i
        # Return -1 if no unique character exists
        return -1

        ## 2. Hash Map: O(n) time and O(n) space
        # Initialize a hash map to store the character counts
        char_counts = {}
        # Iterate through the string
        for char in s:
            # Increment the count of the current character
            char_counts[char] = char_counts.get(char, 0) + 1
        # Iterate through the string
        for i in range(len(s)):
            # Check if the current character is unique
            if char_counts[s[i]] == 1:
                # Return the index of the unique character
                return i
        # Return -1 if no unique character exists
        return -1

        ## 3. Hash Map with Ordered Dictionary: O(n) time and O(n) space
        # Initialize an ordered dictionary to store the character counts
        char_counts = collections.OrderedDict()
        # Iterate through the string
        for char in s:
            # Increment the count of the current character
            char_counts[char] = char_counts.get(char, 0) + 1
        # Iterate through the ordered dictionary
        for char, count in char_counts.items():
            # Check if the current character is unique
            if count == 1:
                # Return the index of the unique character
                return s.index(char)
        # Return -1 if no unique character exists
        return -1

        ## 4. Hash Map with Counter: O(n) time and O(n) space
        # Initialize a counter to store the character counts
        char_counts = collections.Counter(s)
        # Iterate through the string
        for i in range(len(s)):
            # Check if the current character is unique
            if char_counts[s[i]] == 1:
                # Return the index of the unique character
                return i
        # Return -1 if no unique character exists
        return -1

        
            